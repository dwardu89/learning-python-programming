__author__ = 'edwardvella'


def bubble_sort(arr):
    """
    Performs a bubble sort algorithm.
    :param arr: an unsorted array
    :return: a sorted array
    """
    arr_len = len(arr)
    swaps = True
    while swaps:
        swaps = False
        for i in range(0, arr_len - 1):
            if arr[i] > arr[i + 1]:
                # swap the items
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                swaps = True
    return arr


def heap_sort(arr):
    """
    Performs a heap sort algorithm
    :param arr: an unsorted array
    :return: a sorted array
    """
    from Sorting.HeapSorting import HeapSorting
    heap = HeapSorting(arr)
    for i in range(0, len(arr))[::-1]:
        heap.swap(0, i)
        heap.heap_size -= 1
        heap.max_heapify(0)
    return heap.A


def quick_sorting(arr):
    """
    Performs a quick sort algorithm
    :param arr: an unsorted array
    :return: a sorted array
    """
    from Sorting.QuickSorting import QuickSort
    quicksort = QuickSort(arr)
    quicksort.quick_sort(0, len(arr) - 1)
    return quicksort.A


array = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
target_array = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
quick_sorting(array)
