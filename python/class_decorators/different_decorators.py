from decotools import tracer, timer


def decorate_all(decorator):
    def decorate_class(cls):
        for attr, attrval in cls.__dict__.items():
            if callable(attrval):
                setattr(cls, attr, decorator(attrval))
        return cls
    return decorate_class


@decorate_all(timer())
class Person():
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
    lil = Person('Lily Henderson', 80000)

    print(bob.name, sue.name)
    sue.give_raise(.10)
    print('%.2f' % sue.pay)
    print(bob.last_name(), sue.last_name())

    print('%.9f' % Person.__init__.alltime)
