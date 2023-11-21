#!/usr/bin/python3
"""Define the Node Class ."""


class Node:
    def __init__(self, data, next_node=None):
        """
        The node class accepte 2 args:
        data: the data stored
        next_node: ptr to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """this methode serve as getter"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """this methode serve a setter"""
        if (not isinstance(value, int)):
            raise TypeError("data must be integer")
        self.__data = value

    @property
    def next_node(self):
        """this methode serve as getter of next node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """the setter of the Next node"""
        if (not isinstance(value, Node) and value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """this a def of SinglyLinkedList Class"""

    def __init__(self):
        """Init of the singlyLinkedList class
            args:
            head-> the head of the node
        """
        self.__head = None

    def sorted_insert(self, value):
        """this methode tries to insert a node in the corrcet order

        Args:
            value (_Node_):  the node given
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Print the singlilinkedlsit"""
        value = []
        head = self.__head
        while (head is not None):
            value.append(str(head.data))
            head = head.next_node
        return ("\n".join(value))
