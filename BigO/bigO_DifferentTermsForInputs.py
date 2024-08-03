#!/usr/bin/env python3


def print_items(a, b):
    for i in range(a):                  # This would be O(a)
        print(i)
                                                                              # The result of these two would be O(a + b)
    for j in range(b):                 # This would be O(b)
        print(j)



def print_items(a, b):
    for i in range(a):                  # This would be O(a)
        for j in range(b):              # This would be O(b)
            print(i, j)                 # The result of these two would be O(a * b)