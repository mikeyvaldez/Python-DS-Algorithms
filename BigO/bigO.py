#!/usr/bin/env python3

# Big O is always measuring worst case
###############################################
# if n = 1 BigO Values                        #
# O(1)   =  1        --> Constant             # Good
# O(log n) ~ 7       --> Divide and Conquer   # Good
# O(n)   = 100       --> Proportional         # Bad
# O(n^2) = 10,000    --> Loop within a Loop   # Horrible
###############################################
# To see bigO complexity charts https://www.bigocheatsheet.com/

# O(n)
def print_items(n):
    for i in range(n):
        print(i)

print_items(10)