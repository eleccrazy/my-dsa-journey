"""
File: reverse_string_two_pointer.py
Description: This module contains a function to reverse the order of words in a string using a two-pointer approach.
Author: Gizachew Kassa
Date: 02/05/2025
"""


def reverseWords(self, s: str) -> str:
    """
    Reverses the order of words in a given string without using slicing.

    Splits the input string into a list of words, reverses the list in-place
    using a two-pointer approach, and joins it back into a single string with
    single spaces.

    Time Complexity: O(n), where n is the length of the input string.
    Space Complexity: O(n), due to the list of words.
    """
    s_list = s.split()
    left, right = 0, len(s_list) - 1
    while left < right:
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1
    return " ".join(s_list)
