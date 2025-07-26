"""
File: fibonacci_series.py
Description: This module generates Fibonacci numbers using dynamic programming.
Author: Gizachew Kassa
Date: 24-07-2025
"""


def fib(n: int) -> int:
    """
    Calculates the nth Fibonacci number using top-down dynamic programming
    with memoization to avoid redundant recursive calls.

    Time Complexity: O(n)
    - Each Fibonacci number from 0 to n is computed only once and stored.

    Space Complexity: O(n)
    - Memoization dictionary stores up to n values on the call stack.
    """
    memo_dict = {0: 0, 1: 1}

    def helper(x):
        if x in memo_dict:
            return memo_dict[x]
        memo_dict[x] = helper(x - 1) + helper(x - 2)
        return memo_dict[x]

    return helper(n)
