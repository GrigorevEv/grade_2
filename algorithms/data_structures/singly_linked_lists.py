class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class SinglyLindedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = self.head = node
        self.size += 1
        print(f'appended {data}')

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            print(f'iter {val}')
            yield val

    def delete(self, data):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                print(f'deleted {data}')
                return
            prev = current
            current = current.next

    def search(self, data):
        for node in self.iter():
            if data == node:
                print(f'searched {data}')
                return True
        return False

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0
        print('clearing')


if __name__ == '__main__':
    words = SinglyLindedList()
    words.append('egg')
    words.append('spam')
    words.append('ham')

    print()
    words.search('spam')

    print()
    gen = words.iter()
    next(gen)
    next(gen)

    print()
    print(f'before deleting count={words.size}')
    words.delete('spam')
    print(f'after deleting count={words.size}')

    print()
    print(f'before clearing count={words.size}')
    words.clear()
    print(f'after clearing count={words.size}')
