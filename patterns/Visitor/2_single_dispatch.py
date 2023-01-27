from functools import singledispatch
from typing import Callable, List


# Components
class Component:
    def accept(self, visitor: Callable):
        return visitor(self)


class ComponentA(Component):
    def method_a(self):
        print('Method of component A')


class ComponentB(Component):
    def method_b(self):
        print('Method of component B')


# Visitor
@singledispatch
def generate_xml():
    pass


@generate_xml.register
def _(component: ComponentA):
    print('Generate xml for ComponentA')
    print(f'Object is {component}')
    component.method_a()


@generate_xml.register
def _(component: ComponentB):
    print('Generate xml for ComponentB')
    print(f'Object is {component}')
    component.method_b()


# Client code
def client_code(components: List[Component], visitor: Callable):
    for component in components:
        print('---------------------------')
        component.accept(visitor)


if __name__ == '__main__':
    components = [ComponentA(), ComponentB()]
    client_code(components, generate_xml)
    print('Done!')
