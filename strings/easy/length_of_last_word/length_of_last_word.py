"""
File: length_of_last_word.py
Description: This module contains a function to find the length of the last word in a string.
Author: Gizachew Kassa
Date: 03/05/2025
"""


def lengthOfLastWord(self, s: str) -> int:
    """
    Returns the length of the last word in a given string.
    A word is defined as a maximal substring consisting of non-space characters.
    The function first splits the string into words using split(), which handles
    leading, trailing, and multiple spaces. It then checks if there are any words
    present and returns the length of the last word. If there are no words, it
    returns 0.

    Time Complexity: O(n), where n is the length of the input string.
    Space Complexity: O(n), due to the list of words created by split().
    """
    s_list = s.split()
    if len(s_list) < 1:
        return 0
    return len(s_list[-1])
