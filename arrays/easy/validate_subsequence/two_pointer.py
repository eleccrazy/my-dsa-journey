"""
File: two_pointer.py

Description:
Optimized solution for the Validate Subsequence problem using a controlled pointer scan approach.

Author: Gizachew Kassa
Date: 2025-04-25
"""


def isValidSubsequence(array, sequence):
    """
    Checks if the given sequence is a valid subsequence of the array.

    This approach uses a moving start pointer to efficiently scan the array,
    ensuring each element is only visited once.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Returns:
        bool: True if sequence is a valid subsequence of array, False otherwise.
    """
    start = 0
    for x in sequence:
        is_match = False
        for i in range(start, len(array)):
            if array[i] == x:
                start = i + 1
                is_match = True
                break
        if not is_match:
            return False
    return True
