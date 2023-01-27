from heap import Heap


def heap_sort(unsorted_list, heap=Heap()):
    for i in unsorted_list:
        heap.insert(i)
    return [heap.pop() for _ in range(heap.size)]
