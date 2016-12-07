__author__ = 'edwardvella'


class Node:

    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def get_value(self):
        """
        Gets the value of the current node
        :return: the value of the current n
        """
        return self.value

    def next_node(self):
        """
        Gets the next node
        :return: the node on the right of the current one
        """
        return self.right

    def has_next_node(self):
        """
        Checks whether there is a node after the current one
        :return: true if there is a node, false if there isn't a node
        """
        return self.right is not None

    def previous_node(self):
        """
        Gets the previous node
        :return: returns the previous node
        """
        return self.left

    def is_head(self):
        """
        Determines whether the node is the at the head of the list
        :return: true if at head, false if not at head
        """
        return self.left is None

    def is_tail(self):
        """
        Determines whether the node is at the end of the list
        :return: true if at end, false if not at end
        """
        return self.right is None

    def set_next(self, node):
        """
        Sets the right side of the current node
        :param node: the node to set for the right side of the current node
        :return: None
        """
        self.right = node

    def set_previous(self, node):
        """
        Sets the left side of the current node
        :param node: the node to set for the left side of the current node
        :return: None
        """
        self.left = node


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_value(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.has_next_node():
                current_node = current_node.next_node()
                current_node.set_next(Node(value))

    def print_values(self):
        current_node = self.head
        while current_node is not None:
            print current_node.get_value()
            current_node = current_node.get_right()

    def get_tail(self):
        current_node = self.head
        while current_node.has_next_node():
            current_node = current_node.next_node()
        return current_node

    def search_for_value(self, value):
        current_node = self.head
        while current_node is not None and current_node.get_value() != value:
            current_node = current_node.next_node()
        return current_node

    def get_position_for_value(self, value):
        index = 0
        current_node = self.head
        while current_node is not None and current_node.get_value() != value:
            current_node = current_node.next_node()
            index += 1
        if current_node is not None:
            return -1
        return current_node

    def delete_node(self, node):
        if node.previous_node() is not None:
            node.previous_node().set_next(node.next_node())
        else:
            self.head = node.next_node()
        if node.has_next_node():
            node.next_node().set_previous(node.previous_node())
