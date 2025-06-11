"""
File: merge_strings_alternatively.py
Description: This module contains a function to merge two strings alternatively.
Author: Gizachew Kassa
Date: 11-06-2025
"""


def mergeAlternately(self, word1: str, word2: str) -> str:
    """
    Merges two strings by alternating characters from each.
    If one string is longer, appends the remaining characters at the end.

    Time Complexity: O(n)
    - n is the total length of both strings combined

    Space Complexity: O(n)
    - Result string grows linearly with input size
    """
    word1_len = len(word1)
    word2_len = len(word2)
    result = ""
    min_length = min(word1_len, word2_len)

    for i in range(min_length):
        result += word1[i]
        result += word2[i]

    if word1_len > word2_len:
        result += word1[min_length:]
    elif word2_len > word1_len:
        result += word2[min_length:]

    return result
