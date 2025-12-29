"""
Shallow vs Deep Copy Example

This script demonstrates the difference between shallow and deep copies using a nested list.

Key idea:
- Shallow copy shares inner lists
- Deep copy duplicates inner lists

Note: Shallow vs deep copy only matters for mutable objects (lists, dicts, sets, custom objects). Integers are immutable in Python. copy.deepcopy() has no effect on immutable types.
"""

import copy


def shallow_copy_example():
    print("=== Shallow Copy Example ===")

    a = [[1, 2, 3], [4, 5, 6]]

    # Creating a shallow copy of the nested list 'a'
    # Method 1
    b = a.copy()
    # Method 2:  b = a    -> assignment statements create references to the same object rather than copying it
    # Method 3:  b = a[:] -> using slicing

    # Modifying an element in the shallow-copied list
    b[0][0] = 99

    print("Shallow copy (b):", b) #[[99, 2, 3], [4, 5, 6]]
    print("Original (a):   ", a)  # [[99, 2, 3], [4, 5, 6]]  ← original changed
    print()


def deep_copy_example():
    print("=== Deep Copy Example ===")

    a = [[1, 2, 3], [4, 5, 6]]

    # Creating a deep copy of the nested list 'a'
    b = copy.deepcopy(a)

    # Modifying an element in the deep-copied list
    b[0][0] = 99

    print("Deep copy (b):  ", b)  # [[99, 2, 3], [4, 5, 6]]
    print("Original (a):   ", a)  # [[1, 2, 3], [4, 5, 6]]  ← original unchanged
    print()


if __name__ == "__main__":
    shallow_copy_example()
    deep_copy_example()
