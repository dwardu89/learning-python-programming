__author__ = 'edwardvella'


class QuickSort(object):
    """
    This class is used for the quick sorting algorithm found in Sorter.py
    which is defined by the function name quick_sort().
    """
    def __init__(self, arr):
        self.A = arr

    def swap(self, i, j):
        tmp = self.A[i]
        self.A[i] = self.A[j]
        self.A[j] = tmp

    def partition(self, p, r):
        x = self.A[r]
        i = p - 1
        for j in range(p, r):
            if self.A[j] <= x:
                i += 1
                self.swap(i, j)
        self.swap(i + 1, r)
        return i + 1

    def quick_sort(self, p, r):
        """
        The function to call in order to run the quick sorting algorithm
        :param p: the start of the index where to sort
        :param r: the end of the index where to sort
        :return: None
        """
        if p < r:
            q = self.partition(p, r)
            self.quick_sort(p, q - 1)
            self.quick_sort(q, r)
