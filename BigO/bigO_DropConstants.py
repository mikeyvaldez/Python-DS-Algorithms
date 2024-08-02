#!/usr/bin/env python3

# Big O is always measuring worst case


# O(n)
# with the two for loops that iterate one after the other, which are both O(n)
# the math would look something like this:
# O(n) + O(n) -> n + n -> O(2n) drop the constant to simplify -> O(n)
def print_items(n):
    for i in range(n):
        print(i)
    
    for j in range(n):
        print(j)

print_items(10)