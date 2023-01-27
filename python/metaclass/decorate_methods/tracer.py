from decotools import tracer

DO_TRACE = True


class MetaTrace(type):
    def __new__(cls, name, supers, classdict):
        for attr, attrval in classdict.items():
            if DO_TRACE and callable(attrval):
                classdict[attr] = tracer(attrval)
        return type.__new__(cls, name, supers, classdict)


class Person(metaclass=MetaTrace):
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)

    def last_name(self):
        return self.name.split()[-1]


if __name__ == '__main__':
    bob = Person('Bob Smith', 50000)
    sue = Person('Sue Jones', 100000)

    print(bob.name, sue.name)
    sue.give_raise(.10)
    print('%.2f' % sue.pay)
    print(bob.last_name(), sue.last_name())
