"""
File: spiral_matrix.py
Description: This module contains a function to return the elements of a matrix in spiral order.
Author: Gizachew Kassa
Date: 15-06-2025
"""

from typing import List


def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    """
    Traverses a 2D matrix in spiral order and returns the elements in a list.

    Time Complexity: O(m * n)
    - Each element is visited exactly once.

    Space Complexity: O(1) extra (excluding result list)
    - Uses constant space to track boundaries and direction.

    Returns:
        List[int]: Elements of the matrix in spiral order.
    """
    m, n = len(matrix), len(matrix[0])
    i, j = 0, 0
    result = []

    # Define spiral boundaries
    top, bottom, right, left = 0, m, n, -1
    direction = "RIGHT"  # Possible directions: RIGHT, DOWN, LEFT, UP

    while len(result) < m * n:
        if direction == "RIGHT":
            while j < right:
                result.append(matrix[i][j])
                j += 1
            i, j = i + 1, j - 1
            right -= 1
            direction = "DOWN"

        elif direction == "DOWN":
            while i < bottom:
                result.append(matrix[i][j])
                i += 1
            i, j = i - 1, j - 1
            bottom -= 1
            direction = "LEFT"

        elif direction == "LEFT":
            while j > left:
                result.append(matrix[i][j])
                j -= 1
            i, j = i - 1, j + 1
            left += 1
            direction = "UP"

        else:  # UP
            while i > top:
                result.append(matrix[i][j])
                i -= 1
            i, j = i + 1, j + 1
            top += 1
            direction = "RIGHT"

    return result
