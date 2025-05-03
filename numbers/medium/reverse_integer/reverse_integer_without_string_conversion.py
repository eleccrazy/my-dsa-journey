"""
File: reverse_integer_without_string_conversion.py
Description: This module contains a function to reverse the digits of a signed 32-bit integer
without using string conversion.
Author: Gizachew Kassa
Date: 03/05/2025
"""


def reverse(self, x: int) -> int:
    """
    Reverses a 32-bit signed integer using arithmetic operations only.

    Handles sign, extracts digits using modulo and division, and checks for
    overflow without converting to string.

    Time Complexity: O(n), where n is the number of digits in x.
    Space Complexity: O(1)
    """
    is_negative = False
    reversed_x = 0

    if x < 0:
        x *= -1
        is_negative = True

    while x != 0:
        last_digit = x % 10
        reversed_x = reversed_x * 10 + last_digit
        x //= 10

    if is_negative:
        reversed_x *= -1

    if reversed_x < -(2**31) or reversed_x > 2**31 - 1:
        return 0

    return reversed_x
