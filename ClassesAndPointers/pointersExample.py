#!/usr/bin/env python3

# Remember integers are immutable: meaning they cannot be changed



# num1 = 11

# num2 = num1

# print("Before num2 value is updated:")
# print("num1 =", num1)
# print("num2 =", num2)

# print("\nnum1 points to:", id(num1))
# print("\nnum2 points to:", id(num2))

# num2 = 22

# print("\nAfter num2 value is updated:")
# print("num1 =", num1)
# print("num2 =", num2)

# print("\nnum1 points to:", id(num1))
# print("\nnum2 points to:", id(num2))

############################################################################

# Remember dictionaries are mutable: meaning they can be changed.
# linked lists are like dictionaries so they can be changed.

# what happens to the dictionary when a variable is no longer pointing at it?
# Python will remove the dictionary through a process called garbage collection

dict1 = {
    'value': 11
}

dict2 = dict1

print("Before value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("\ndict2 points to:", id(dict2))

dict2['value'] = 22

print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("\ndict2 points to:", id(dict2))
