import unittest

from DataStructures.BinaryTree import BinaryTree

__author__ = 'edwardvella'


class BinaryTreeTestCase(unittest.TestCase):
    def setUp(self):
        self.binary_tree = BinaryTree()


class SingleInsertionTestCase(BinaryTreeTestCase):
    def runTest(self):

        to_insert = 1
        self.binary_tree.insert(to_insert)
        self.assertIsNotNone(self.binary_tree.head)
        self.assertEqual(to_insert, self.binary_tree.head.get_value())


class DoubleInsertionLeft(BinaryTreeTestCase):
    def runTest(self):

        to_insert_head = 2
        to_insert_left = 1
        self.binary_tree.insert(to_insert_head)
        self.binary_tree.insert(to_insert_left)
        self.assertIsNotNone(self.binary_tree.head)
        self.assertEqual(to_insert_head, self.binary_tree.head.get_value())
        self.assertEqual(to_insert_left, self.binary_tree.head.get_left().get_value())
        self.binary_tree.print_tree()


class TwoItemList(BinaryTreeTestCase):
    def runTest(self):
        expected = [1, 2]
        to_insert_head = 2
        to_insert_left = 1
        self.binary_tree.insert(to_insert_head)
        self.binary_tree.insert(to_insert_left)
        self.assertIsNotNone(self.binary_tree.head)
        self.assertEqual(to_insert_head, self.binary_tree.head.get_value())
        self.assertEqual(to_insert_left, self.binary_tree.head.get_left().get_value())
        actual_list = self.binary_tree.get_list()
        self.assertEquals(len(actual_list), 2)
        self.assertItemsEqual(expected, actual_list, 'The list is not in the correct order {}'.format(expected))


if __name__ == '__main__':
    unittest.main()
