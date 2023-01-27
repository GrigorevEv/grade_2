import time
import random
import copy
import multiprocessing

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from quick_sort import quick_sort
from heap_sort import heap_sort
from merge_sort import merge_sort
from python_sort import python_sort


def print_time(sort_func, list_to_sort):
    func_name = sort_func.__name__
    list_to_sort = copy.copy(list_to_sort)
    start = time.time()
    sort_func(list_to_sort)
    print(f'{func_name} --> {time.time() - start}')


if __name__ == '__main__':
    L = [random.randint(0, 100000) for _ in range(10000)]

    for func in (
        selection_sort,
        bubble_sort,
        insertion_sort,
        heap_sort,
        merge_sort,
        quick_sort,
        python_sort,
    ):
        multiprocessing.Process(target=print_time, args=(func, L)).start()
