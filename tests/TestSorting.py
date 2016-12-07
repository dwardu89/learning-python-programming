import unittest

__author__ = 'edwardvella'


class TestSorting(unittest.TestCase):
    def test_bubble_sort(self):
        from Sorting.Sorter import bubble_sort
        array = [1, 3, 10, 2, 50, 222, 20101]
        target_array = [1, 2, 3, 10, 50, 222, 20101]
        self.assertEqual(target_array, bubble_sort(array))

    def test_heap_sort(self):
        from Sorting.Sorter import heap_sort
        array = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        target_array = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
        self.assertEqual(target_array, heap_sort(array))

    def test_quick_sort(self):
        from Sorting.Sorter import quick_sorting
        array = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        target_array = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
        self.assertEqual(target_array, quick_sorting(array))


if __name__ == '__main__':
    unittest.main()
