"""
File: climbing_stairs_optimized.py
Description: This module calculates the number of distinct ways to climb a staircase using
             space optimized bottom-up dynamic programming approach.
Author: Gizachew Kassa
Date: 26-07-2025
"""


def climbStairs(n: int) -> int:
    """
    Computes the number of distinct ways to climb a staircase of n steps,
    where you can take either 1 or 2 steps at a time.

    This implementation uses bottom-up dynamic programming with constant space.

    Time Complexity: O(n)
    - Iterates from step 3 to n

    Space Complexity: O(1)
    - Only stores results for the two previous steps
    """
    if n < 3:
        return n

    one_step_before = 2  # f(n-1)
    two_steps_before = 1  # f(n-2)

    for _ in range(3, n + 1):
        current = one_step_before + two_steps_before
        two_steps_before = one_step_before
        one_step_before = current

    return one_step_before
