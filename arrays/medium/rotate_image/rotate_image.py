"""
File: rotate_image.py
Description: This module contains a function to rotate a 2D matrix (image) by 90 degrees clockwise.
Author: Gizachew Kassa
Date: 15-06-2025
"""

from typing import List


def rotate(self, matrix: List[List[int]]) -> None:
    """
    Rotates the given n x n matrix by 90 degrees clockwise in-place.

    Time Complexity: O(n^2)
    - Transposing and reversing each row touches all elements once.

    Space Complexity: O(1)
    - Rotation is performed in-place without using extra space.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix (flip over its diagonal)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row (mirror horizontally)
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
