class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self._float(self.size)

    def pop(self):
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self._sink(1)
        return item

    def _float(self, k):
        while k // 2 > 0:
            if self.heap[k] < self.heap[k // 2]:
                self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]
            k //= 2

    def _min_index(self, k):
        if k * 2 + 1 > self.size:
            return k * 2
        elif self.heap[k * 2] < self.heap[k * 2 + 1]:
            return k * 2
        else:
            return k * 2 + 1

    def _sink(self, k):
        while k * 2 <= self.size:
            mi = self._min_index(k)
            if self.heap[k] > self.heap[mi]:
                self.heap[k], self.heap[mi] = self.heap[mi], self.heap[k]
            k = mi


if __name__ == '__main__':
    h = Heap()
    for i in (4, 8, 7, 2, 9, 10, 5, 1, 3, 6):
        h.insert(i)
        print(h.heap)

    print()
    print()

    print(h.heap)
    for i in range(10):
        n = h.pop()
        print(n)
        print(h.heap)
