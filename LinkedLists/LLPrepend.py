#!/usr/bin/env python3

# This creates an empty node
class Node:
    def __init__(self, value):      
        self.value = value
        self.next = None

# This is the Linked List Contructor
class LinkedList:
    def __init__(self, value):      # There will always be self as one of the parameters. This is how you can tell this is a method inside of a class. instead of a regular function
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

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True      # This line is optional
    

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp


my_linked_list = LinkedList(2)
my_linked_list.append(3)

# (2) Items - Returns 2 Node
print(my_linked_list.pop_first())
# (1) Item - Returns 1 Node
print(my_linked_list.pop_first())
#(0) Items - Returns None
print(my_linked_list.pop_first())

my_linked_list.print_list()
