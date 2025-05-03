"""
File: reverse_integer.py
Description: This module contains a function to reverse the digits of a signed 32-bit integer.
Author: Gizachew Kassa
Date: 03/05/2025
"""


def reverse(self, x: int) -> int:
    """
    Reverses the digits of a signed 32-bit integer.

    If the reversed integer overflows the 32-bit signed integer range,
    returns 0 instead.

    Time Complexity: O(n), where n is the number of digits in x.
    Space Complexity: O(n), due to string conversion and slicing.
    """
    is_negative = False
    if x < 0:
        x *= -1
        is_negative = True

    x_str = str(x)
    x_reversed = int(x_str[::-1])

    if is_negative:
        x_reversed *= -1

    if x_reversed < -(2**31) or x_reversed > 2**31 - 1:
        return 0

    return x_reversed
