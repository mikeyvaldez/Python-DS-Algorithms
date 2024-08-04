#!/usr/bin/env python3


# This creates an empty node
class Node:
    def __init__(self, value):      
        self.value = value
        self.next = None

# This is the Linked List Contructor
class LinkedList:
    def __init__(self, value):      # There will always be self as one of the parameters. This is how you cantell this is a method inside of a class. instead of a regular function
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        #return True  # This line is optional,


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.print_list()