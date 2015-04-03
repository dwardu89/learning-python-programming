__author__ = 'edwardvella'
import unittest


class TestSorting(unittest.TestCase):

    def test_bubble_sort(self):
        from Sorting import bubble_sort
        array = [1 ,3, 10, 2, 50, 222, 20101]
        target_array = [1, 2, 3, 10, 50, 222, 20101]
        self.assertEqual(target_array, bubble_sort(array))

if __name__ == '__main__':
    unittest.main()