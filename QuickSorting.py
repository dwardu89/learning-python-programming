__author__ = 'edwardvella'


class QuickSort(object):

    def __init__(self, arr):
        self.A = arr

    def swap(self, i, j):
        tmp = self.A[i]
        self.A[i] = self.A[j]
        self.A[j] = tmp

    def partition(self, p, r):
        x = self.A[r]
        i = p - 1
        for j in range(p, r - 1):
            if self.A[j] <= x:
                i = i + 1
                self.swap(i, j)
        self.swap(i + 1, r)
        return i + 1

    def quicksort(self, p, r):
        if p < r:
            q = self.partition(p, r)
            self.quicksort(p, q - 1)
            self.quicksort(q + 1, r)
