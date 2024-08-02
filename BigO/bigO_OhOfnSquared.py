#!/usr/bin/env python3

# Big O is always measuring worst case


# O(n^2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

print_items(10)