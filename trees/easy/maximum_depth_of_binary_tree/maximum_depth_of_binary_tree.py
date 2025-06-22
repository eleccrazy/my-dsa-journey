# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the maximum depth of a binary tree using recursion.

        Time Complexity: O(n)
        - Each node is visited exactly once.

        Space Complexity: O(h)
        - Where h is the height of the tree due to recursion stack.
        - Worst-case: O(n) for a skewed tree; Best-case: O(log n) for balanced.

        Returns:
            int: Maximum depth of the binary tree.
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
