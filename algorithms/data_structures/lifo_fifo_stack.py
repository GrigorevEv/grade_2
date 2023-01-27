from collections import deque
from collections.abc import Iterable
from typing import Optional

# Очереди и стек могут быть основаны на динамическом массиве,
# но лучше взять за основу двусвязный список (deque), т.к. он будет
# выгднее по памяти и производительности.
# Stack это тот же Lifo но с огранниченным функционалом, не имеет
# доступ к элементам кроме последнего


class Queue:
    def __init__(self, data: Optional[Iterable] = None):
        self.dq = deque(data if data else ())

    def append(self, value):
        self.dq.append(value)

    def insert(self, position: int, value):
        self.dq.insert(position, value)

    def __str__(self):
        cls_name = self.__class__.__name__
        return f'<{cls_name} {self.dq}>'


class Lifo(Queue):
    def pop(self):
        try:
            return self.dq.pop()
        except IndexError:
            return


class Fifo(Queue):
    def pop(self):
        try:
            return self.dq.popleft()
        except IndexError:
            return


class Stack:
    def append(self, value):
        self.dq.append(value)

    def pop(self):
        try:
            return self.dq.pop()
        except IndexError:
            return


if __name__ == '__main__':
    data = (1,2,3,4,5)

    # Lifo
    lifo = Lifo(data)
    print(lifo)
    lifo.append(6)
    print(lifo)
    print(lifo.pop())
    print(lifo)
    lifo.insert(2, 8)
    print(lifo)
    print()
    print()

    # Fifo
    fifo = Fifo(data)
    print(fifo)
    fifo.append(6)
    print(fifo)
    print(fifo.pop())
    print(fifo)

