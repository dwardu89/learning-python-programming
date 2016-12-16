__author__ = 'edwardvella'


class Node:
    def __init__(self, value):
        self. value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def get_left(self):
        return self.left

    def set_left(self, node):
        self.left = node

    def get_right(self):
        return self.right

    def set_right(self, node):
        self.right = node


class BinaryTree:


    """This is a sorted Binary Tree, values on the left side
    of a node is smaller than the value of the parent node.
    The right side holds the nodes that have a larger value.
    This tree will not have duplicate values.
    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        """
        Inserts a value into the binary tree.
        This is an iterative approach of the solution, there are other ways to
        get this solved.
        :param value: the value to insert.
        :return: None
        """
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while True and current_node.get_value() is not value:
                if current_node.get_value() > value:
                    if current_node.get_left() is None:
                        current_node.set_left(Node(value))
                    current_node = current_node.get_left()
                else:
                    if current_node.get_right() is None:
                        current_node.set_right(Node(value))
                    current_node = current_node.get_right()

    def _print_tree(self, node):
        if node.get_left() is not None:
            self._print_tree(node.get_left())

        print node.get_value()

        if node.get_right() is not None:
            self._print_tree(node.get_right)

    def print_tree(self):
        self._print_tree(self.head)

    def _get_list(self, node, lst):
        if node.get_left() is not None:
            lst = self._get_list(node.get_left(), lst)

        lst.append(node.get_value())

        if node.get_right() is not None:
            lst = self._get_list(node.get_right, lst)

        return lst

    def get_list(self):
        lst = []
        lst = self._get_list(self.head, lst)
        return lst
