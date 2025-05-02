"""
File: reverse_string.py
Description: This module contains a function to reverse a string in place.
Author: Gizachew Kassa
Date: 02/05/2025
"""


def reverseWords(self, s: str) -> str:
    """
    Reverses the order of words in a given string, removing leading, trailing,
    and extra intermediate spaces.

    The string is first split into words using split(), which handles all spacing issues.
    Then the list of words is reversed and joined back into a single space-separated string.

    Time Complexity: O(n), where n is the length of the input string.
    Space Complexity: O(n), due to the list of words stored in memory.
    """
    string_list = s.split()
    string_list[:] = string_list[::-1]
    return " ".join(string_list)
