#!/usr/bin/python3
""" singly linked list"""


class Node:
    """class that defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Instantiation with size"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieves data"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets data"""
        if type(value) is not int:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        """retrieves next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets next node"""
        if value is not None and type(value) is not Node:
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value


class SinglyLinkedList:
    """class that defines a singly linked list"""
    def __init__(self):
        """Simple instantiation"""
        self.__head = None
        self.linked_list = []

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position in the list"""
        new_node = Node(value)
        new_node.next_node = self.__head
        self.__head = new_node
        self.linked_list = []
        temp = Node(self.__head.data, self.__head.next_node)
        while temp is not None:
            self.linked_list.append(temp.data)
            temp = temp.next_node
        self.linked_list.sort()

    def __str__(self):
        """returns string"""
        return '\n'.join(list(map(str, self.linked_list)))
