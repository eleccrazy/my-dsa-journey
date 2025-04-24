"""
File: brute_force.py
Description: This module contains a brute force solution to the Validate Subsequence problem.
Author: Gizachew Kassa
Date: 2025-04-25
"""

from typing import List


def isValidSubsequence(array: List[int], sequence: List[int]) -> bool:
    """
    Returns True if the sequence is a valid subsequence of the array.

    A valid subsequence is derived from the array by deleting some elements without changing the order of the remaining elements.
    This brute force approach checks if all elements of the sequence are present in the array in the same order.

    Time Complexity: O(n^2)
    Space Complexity: O(n)
    Returns:
        True if the sequence is a valid subsequence of the array, False otherwise.
    """
    sub_array = []
    sequence_copy = [n for n in sequence]
    n = len(sequence)
    count = 0
    for num in array:
        if num in sequence:
            sub_array.append(num)
            sequence.remove(num)
    if n != len(sub_array):
        return False
    for i in range(n):
        if sub_array[i] != sequence_copy[i]:
            return False
    return True
