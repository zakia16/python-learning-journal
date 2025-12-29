"""
Shallow Copy Example - Normal List

This script demonstrates the difference between shallow and normal copies using a normal (non-nested) list.
"""

import copy

def shallow_copy_list():
    print("=== Shallow Copy Example (Normal List) ===")

    a = [1, 2, 3, 4]

    # Shallow copy
    b = a.copy()    # If I use b = a, it will change the original, that's why I need a shallow copy  or I can create a new list

    # Modify copied list
    b[0] = 99

    print("Shallow copy (b):", b)
    print("Original list (a):", a)  # Original remains unchanged
    print()


if __name__ == "__main__":
    shallow_copy_list()
