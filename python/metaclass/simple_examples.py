print('1---------------------------------------------------')


REQUIRED = True
# REQUIRED = False

def foo(self, name: str):
    print(f'foo {name}')


class Extras(type):
    def __init__(Class, classname, superclasses, attributedict):
        if REQUIRED:
            Class.foo = foo

class A(metaclass=Extras): ...

class B(metaclass=Extras): ...

a = A()
b = B()

a.foo('bla_bla')
b.foo('bla_bla_2')


print('2---------------------------------------------------')

class Eggs:
    pass

Spam = type('Spam', (Eggs,), {'data': 1, 'meth': (lambda x, y: x.data + y)})
i = Spam()

print(Spam.__mro__, Spam.__dict__)
print(i.__class__)

print('3---------------------------------------------------')

class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new:', meta, classname, supers, classdict, sep='\n...')
        return type.__new__ (meta, classname, supers, classdict)
    def __init__ (Class, classname, supers, classdict) :
        print('In MetaTwo.init', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))

class Eggs:
    pass

print('making class')

class Spam(Eggs, metaclass=MetaOne):
    data = 1
    def meth(self, arg):
        return self.data + arg

print('making instatce')
x = Spam()
print('data:', x.data, x.meth(3))


print('4---------------------------------------------------')

def eggsfunc(obj):
    return obj.value * 4

def hamfunc(obj, value):
    return value + 'ham'

class Extender(type):
    def __new__(meta, classname, supers, classdict):
        classdict['eggs'] = eggsfunc
        classdict['ham'] = hamfunc
        return type.__new__(meta, classname, supers, classdict)

class Client1(metaclass=Extender):
    def __init__(self, value):
        self.value = value

    def spam(self):
        return self.value * 2

class Client2(metaclass=Extender):
    value = 'ni?'


x = Client1('Ni?')
print(x.spam())
print(x.eggs())
print(x.ham('bacon'))

y = Client2()
print(y.eggs())
print(y.ham('bacon'))
