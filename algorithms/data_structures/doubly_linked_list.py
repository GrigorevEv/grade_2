class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.head
            self.head.next = new_node
            self.head = new_node
        self.size += 1
        print(f'appended {data}')

    def delete(self, data):
        current = self.tail
        node_deleted = False

        if current is None:
            node_deleted = False
        elif current.data == data:
            self.tail = current.next
            self.tail.prev = None
            node_deleted = True
            print(f'deleted {data}')
        elif self.head.data == data:
            self.head = self.head.prev
            self.head.next = None
            node_deleted = True
            print(f'deleted {data}')
        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                    print(f'deleted {data}')
                current = current.next
        if node_deleted:
            self.size -= 1

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            print(f'iter {val}')
            yield val

    def search(self, data):
        for node in self.iter():
            if data == node:
                print(f'contained {data}')
                return True
        return False

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0
        print('clearing')


if __name__ == '__main__':
    words = DoublyLinkedList()
    words.append('egg')
    words.append('spam')
    words.append('ham')

    print()
    words.search('spam')

    print()
    gen = words.iter()
    next(gen)
    next(gen)
    next(gen)

    print()
    print(f'before deleting size={words.size}')
    words.delete('spam')
    print(f'after deleting size={words.size}')

    print()
    print(f'before clearing size={words.size}')
    words.clear()
    print(f'after clearing size={words.size}')
