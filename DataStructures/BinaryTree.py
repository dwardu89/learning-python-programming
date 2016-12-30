__author__ = 'edwardvella'


class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent


class BinaryTree:

    """
    This is a sorted Binary Tree, values on the left side
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
            while True and current_node.value is not value:
                if current_node.value > value:
                    if current_node.left is None:
                        current_node.left = Node(value, current_node)
                    current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = Node(value, current_node)
                    current_node = current_node.right

    def _print_tree(self, node):
        if node.left is not None:
            self._print_tree(node.left)

        print node.value

        if node.right is not None:
            self._print_tree(node.right)

    def print_tree(self):
        self._print_tree(self.head)

    def _get_list(self, node, lst):
        if node.left is not None:
            lst = self._get_list(node.left, lst)

        lst.append(node.value)

        if node.right is not None:
            lst = self._get_list(node.right, lst)

        return lst

    def get_list(self):
        lst = []
        lst = self._get_list(self.head, lst)
        return lst

    def _find_node(self, value, node):
        if node is None:
            return None
        else:
            if node.value == value:
                return node
            else:
                if node.value > value:
                    return self._find_node(value, node.left)
                else:
                    return self._find_node(value, node.right)

    def find_node(self, value):
        return self._find_node(value, self.head)

    def _transplant(self, node, replacement):
        if node.parent is None:
            self.head = replacement
        else:
            if node == node.parent.left:
                node.parent.left = replacement
            else:
                node.parent.right = replacement
            if replacement is not None:
                replacement.parent = node.parent

    def _find_node_with_no_left_child(self, node):
        if node.left is not None:
            return self._find_node_with_no_left_child(node.left)
        else:
            return node

    def _tree_minimum(self, node):
        if node.left is not None:
            return self._tree_minimum(node.left)
        else:
            return node

    def _delete_value(self, node):
        if node.left is None:
            self._transplant(node, node.right)
        else:
            if node.right is None:
                self._transplant(node, node.left)
            else:
                minimum_right_of_node = self._tree_minimum(node.right)
                if minimum_right_of_node.parent != node:
                    self._transplant(minimum_right_of_node, minimum_right_of_node.right)
                    minimum_right_of_node.right = node.right
                    minimum_right_of_node.right.parent = minimum_right_of_node
                self._transplant(node, minimum_right_of_node)
                minimum_right_of_node.left = node.left
                minimum_right_of_node.left.parent = minimum_right_of_node

    def delete_value(self, value):
        to_delete = self.find_node(value)
        if to_delete is not None:
            self._delete_value(to_delete)

