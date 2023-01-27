from decotools import 
print('-------------------------------------------------------------')


def decorator(cls):
    print(f'cls >>>>>> `{cls.__mro__}`')
    return cls


@decorator
class C:
    pass


print('-------------------------------------------------------------')


def log_getattribute(cls):
    orig_getattribute = cls.__getattribute__

    def new_getattribute(self, name):
        print('getting:', name)
        return orig_getattribute(self, name)

    cls.__getattribute__ = new_getattribute
    return cls

@log_getattribute
class A:
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass

a = A(2323)
a.x
a.spam()


print('-------------------------------------------------------------')


import functools


def dec(cls):

    @functools.wraps(cls, updated=())
    class D(cls):
        def foo(self):
            print('fooooooooo')
    return D


@dec
class C:
    """Some doc string."""
    bla: str

    def bar(self):
        print('baaaaaaaar')


c = C()
c.bar()
c.foo()
print(C.__doc__, C.__name__, C.__annotations__)


print('-------------------------------------------------------------')
