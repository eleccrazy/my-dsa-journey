"""
File: string_to_integer.py
Description: This module contains a function to convert a string to a 32-bit signed integer.
Author: Gizachew Kassa
Date: 03/05/2025
"""


def myAtoi(self, s: str) -> int:
    """
    Converts a string to a 32-bit signed integer using custom parsing logic,
    mimicking the behavior of the C 'atoi' function.

    Time Complexity: O(n), where n is the length of the input string
    Space Complexity: O(n), due to string accumulation
    """
    s_trimmed = s.lstrip()
    if not s_trimmed:
        return 0

    is_negative = False
    if s_trimmed[0] in ("-", "+"):
        is_negative = s_trimmed[0] == "-"
        s_trimmed = s_trimmed[1:]

    formed_number = ""
    for ch in s_trimmed:
        if not ch.isdigit():
            break
        formed_number += ch

    result = int(formed_number) if formed_number else 0
    result = -result if is_negative else result

    INT_MIN, INT_MAX = -(2**31), 2**31 - 1
    result = max(INT_MIN, min(result, INT_MAX))

    return result
