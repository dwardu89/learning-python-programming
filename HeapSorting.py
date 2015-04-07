__author__ = 'edwardvella'


class Heap:
    '''
    This class is used for the heap sorting algorithm found in Sorting.py
    which is defined by the function name heap_sort().
    '''
    A = None
    heap_size = None

    def __init__(self, A):
        self.A = A
        self.build_max_heap()

    def build_max_heap(self):
        self.heap_size = len(self.A) - 1
        for i in range(-1, (len(self.A)) / 2)[::-1]:
            self.max_heapify(i)

    def max_heapify(self, i):
        l = left(i)
        r = right(i)
        largest = i
        if l <= self.heap_size:
            if self.A[l] > self.A[i]:
                largest = l
        if r <= self.heap_size:
            if self.A[r] > self.A[largest]:
                largest = r
        if largest != i:
            self.swap(i, largest)
            self.max_heapify(largest)

    def swap(self, i, j):
        temp = self.A[i]
        self.A[i] = self.A[j]
        self.A[j] = temp


def parent(i):
    return i / 2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1