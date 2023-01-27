class DescSquare:
    def __init__(self, degree: int):
        self.degree = degree

    def __get__(self, instance, owner):
        return instance._dig ** self.degree

    def __set__(self, instance, value):
        instance._dig = value


class Client1:
    def __init__(self, dig: int):
        self._dig = dig

    dig = DescSquare(3)


c1 = Client1(23)

print(c1.dig)
c1.dig = 32
print(c1.dig)
