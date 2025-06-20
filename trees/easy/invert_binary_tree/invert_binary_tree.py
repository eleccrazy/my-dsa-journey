"""
File: invert_binary_tree.py
Description: This module contains a function to invert a binary tree.
Author: Gizachew Kassa
Date: 21/06/2025
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Recursively inverts a binary tree in-place by swapping the left and right children
        of each node.

        Time Complexity: O(n)
        - Each node is visited exactly once.

        Space Complexity: O(h)
        - Call stack can grow up to the height of the tree (h), worst-case O(n).

        Returns:
            TreeNode: Root of the inverted binary tree.
        """
        if not root:
            return

        # Swap left and right subtrees
        root.left, root.right = root.right, root.left

        # Recur on left and right children
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)

        return root
