#!/usr/bin/env python3

# Big O is always measuring worst case


# O(n^2)
def print_items(n):
    for i in range(n):
        for j in range(n):              # These for loops = O(n^2)   <-- dominant term
            print(i, j)
                                        #                     +         ---> O(n^2 + n)
                                                               
    for k in range(n):                  # This for loop =    O(n)    <-- Non-dominant term that we drop.
        print(k)

print_items(10)


