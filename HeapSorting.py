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

    def maximum(self):
        return self.A[0]

    def extract_heap_max(self):
        """
        Extracts the maximum heap value and removes it from the heap
        :return: the maximum heap value or raises the heap underflow exception
        """
        if self.heap_size < 1:
            # Heap Underflow exception
            raise HeapUnderflowException("Heap Underflow")
        maximum = self.A[0]
        self.A[0] = self.A[self.heap_size]
        self.heap_size -= 1
        self.max_heapify(0)
        return maximum

    def increase_heap_key(self, i, key):
        """
        Increases the heap key
        :param i: the current index
        :param key: the key
        :return: None, raises KeyException if error
        """
        if key < self.A[i]:
            raise KeyException("New Key is smaller than the current key")
        self.A[i] = key
        while i > 0 and self.A[parent(i)] < self.A[i]:
            self.swap(i, parent(i))
            i = parent(i)

    def max_heap_insert(self, key):
        self.heap_size += 1
        # Since there is no representation of the minimum integer, use the value of a googol * -1
        self.A[self.heap_size] = 10**100 * -1
        self.increase_heap_key(self.heap_size, key)


def parent(i):
    '''
    Gets the parent index
    :param i: the current index
    :return: the parent index
    '''
    return i / 2


def left(i):
    '''
    Gets the child on the left of an index
    :param i: the current index
    :return: the index of the left child
    '''
    return 2 * i


def right(i):
    '''
    Gets the child on the right of an index
    :param i: the current index
    :return: the index of the right child
    '''
    return 2 * i + 1


class HeapUnderflowException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class KeyException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
