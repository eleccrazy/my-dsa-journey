"""
File: plus_one.py
Description: This module contains a function to add one to a number represented as an array of digits.
Author: Gizachew Kassa
Date: 03/05/2025
"""

from typing import List


def plusOne(self, digits: List[int]) -> List[int]:
    """
    Adds one to a number represented as an array of digits.
    The function converts the list of digits into a single integer, adds one to it,
    and then converts it back into a list of digits.

    Time Complexity: O(n), where n is the number of digits in the input list.
    Space Complexity: O(n), due to the space used for the integer conversion and the output list.
    """
    num = int("".join([str(x) for x in digits]))
    one_added_num = num + 1
    return list(int(x) for x in str(one_added_num))
