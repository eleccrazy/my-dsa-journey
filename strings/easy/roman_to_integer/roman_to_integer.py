"""
File: roman_to_integer.py
Description: This module contains a function to convert a Roman numeral string to an integer.
Author: Gizachew Kassa
Date: 03/05/2025
"""


def romanToInt(self, s: str) -> int:
    """
    Converts a Roman numeral string to an integer.

    The function uses a dictionary to map Roman numeral characters to their integer values.
    It iterates through the string in reverse order, adding or subtracting values based on the
    relative values of the current and previous characters.

    Time Complexity: O(n), where n is the length of the input string.
    Space Complexity: O(1), as the space used does not depend on the input size.
    """

    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev = 0

    for c in reversed(s):
        curr = roman_map[c]
        if curr < prev:
            total -= curr
        else:
            total += curr
        prev = roman_map[c]

    return total
