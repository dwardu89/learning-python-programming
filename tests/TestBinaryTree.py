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
        self.assertEqual(to_insert, self.binary_tree.head.value)


class DoubleInsertionLeft(BinaryTreeTestCase):
    def runTest(self):

        to_insert_head = 2
        to_insert_left = 1
        self.binary_tree.insert(to_insert_head)
        self.binary_tree.insert(to_insert_left)
        self.assertIsNotNone(self.binary_tree.head)
        self.assertEqual(to_insert_head, self.binary_tree.head.value)
        self.assertEqual(to_insert_left, self.binary_tree.head.left.value)
        self.binary_tree.print_tree()


class TwoItemList(BinaryTreeTestCase):
    def runTest(self):
        expected = [1, 2]
        to_insert_head = 2
        to_insert_left = 1
        self.binary_tree.insert(to_insert_head)
        self.binary_tree.insert(to_insert_left)
        self.assertIsNotNone(self.binary_tree.head)
        self.assertEqual(to_insert_head, self.binary_tree.head.value)
        self.assertEqual(to_insert_left, self.binary_tree.head.left.value)
        actual_list = self.binary_tree.get_list()
        self.assertEquals(len(actual_list), 2)
        self.assertItemsEqual(expected, actual_list, 'The list is not in the correct order {}'.format(expected))


class TestPopulatedBinaryTree(unittest.TestCase):
    def setUp(self):
        self.binary_tree = BinaryTree()
        self.binary_tree.insert(5)
        self.binary_tree.insert(3)
        self.binary_tree.insert(2)
        self.binary_tree.insert(1)
        self.binary_tree.insert(8)
        self.binary_tree.insert(6)
        self.binary_tree.insert(7)
        self.binary_tree.insert(9)


class TestFindBinaryTreeExistsAtHead(TestPopulatedBinaryTree):
    def runTest(self):
        to_search = 6
        result = self.binary_tree.find_node(to_search)
        self.assertIsNotNone(result)
        self.assertEqual(result.value, to_search)


class TestFindBinaryTreeExistsAtHead(TestPopulatedBinaryTree):
    def runTest(self):
        to_search = 5
        result = self.binary_tree.find_node(to_search)
        self.assertIsNotNone(result)
        self.assertEqual(result.value, to_search)


class TestFindBinaryTreeDoesNotExist(TestPopulatedBinaryTree):
    def runTest(self):
        to_search = 123
        result = self.binary_tree.find_node(to_search)
        self.assertIsNone(result)


class TestBinaryTreeDeleteHead(TestPopulatedBinaryTree):
    def runTest(self):
        expected = 6
        list_length = len(self.binary_tree.get_list())
        self.binary_tree.delete_value(5)
        self.assertEqual(self.binary_tree.head.value, expected)
        self.assertEqual(len(self.binary_tree.get_list()), list_length - 1)


if __name__ == '__main__':
    unittest.main()
