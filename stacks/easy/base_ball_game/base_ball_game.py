"""
File: base_ball_game.py
Description: This module contains a function to calculate the score of a baseball game based on a list of operations.
Author: Gizachew Kassa
Date: 29-06-2025
"""

from typing import List


def calPoints(self, operations: List[str]) -> int:
    """
    Calculates the total score from a list of operations based on custom baseball game rules.

    Time Complexity: O(n)
    - Each operation is processed once.

    Space Complexity: O(n)
    - Stores all valid scores in a list.

    Returns:
        int: The final sum of scores after all operations.
    """
    record = []

    for op in operations:
        if op == "D":
            record.append(2 * record[-1])
        elif op == "C":
            record.pop()
        elif op == "+":
            record.append(record[-1] + record[-2])
        else:
            record.append(int(op))

    return sum(record)
