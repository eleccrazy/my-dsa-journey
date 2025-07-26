"""
File: climbing_stairs.py
Description: This module calculates the number of distinct ways to climb a staircase using dynamic programming.
Author: Gizachew Kassa
Date: 26-07-2025
"""


def climbStairs(n: int) -> int:
    """
    Computes the number of distinct ways to climb a staircase of n steps,
    where you can take either 1 or 2 steps at a time.

    Time Complexity: O(n)
    - Each subproblem from 1 to n is solved once and cached.

    Space Complexity: O(n)
    - Due to memoization dictionary and recursion stack.
    """
    memo_dict = {1: 1, 2: 2}

    def helper_func(x):
        if x in memo_dict:
            return memo_dict[x]
        memo_dict[x] = helper_func(x - 1) + helper_func(x - 2)
        return memo_dict[x]

    return helper_func(n)
