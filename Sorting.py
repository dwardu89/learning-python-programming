__author__ = 'edwardvella'

def bubble_sort(arr):
    '''
    Performs a bubble sort algorithm.
    :param arr: an unsorted array
    :return: a sorted array
    '''
    arr_len = len(arr)
    swaps = True
    while swaps:
        swaps = False
        for i in range(0, arr_len-1):
            if arr[i] > arr[i + 1]:
                #swap the items
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1]  = temp
                swaps = True
    return arr

array = range(1,11)[::-1]

print array
print bubble_sort(array)
