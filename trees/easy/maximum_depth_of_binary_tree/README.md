# Maximum Depth of Binary Tree

## Problem Statement

Given the `root` of a binary tree, return its **maximum depth**.

The **maximum depth** is the number of nodes along the longest path from the **root node** down to the **farthest leaf node**.

---

## Examples

### Example 1
```python
Input: root = [3,9,20,null,null,15,7]
Output: 3
```
**Explanation:**
The longest path from the root node (3) to the farthest leaf node (15 or 7) has a depth of 3.

```
    3
   / \
  9   20
     /  \
    15   7
```
### Example 2
```python
Input: root = [1,null,2]
Output: 2
```
**Explanation:**
The longest path from the root node (1) to the farthest leaf node (2) has a depth of 2.

```
    1
     \
      2
```


---

## Constraints

- The number of nodes in the tree is in the range `[0, 10⁴]`.
- `-100 <= Node.val <= 100`

## Solution Overview

This recursive solution performs a post-order depth-first traversal to calculate the depth of a binary tree.

- At each node, it calculates the depth of its left and right subtrees.
- The depth of the current node is 1 + the maximum of the two.
- Base case: if the node is `null`, depth is 0.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
  - Each of the n nodes is visited exactly once.

- **Space Complexity:** `O(h)`
  - Call stack grows up to the height of the tree (h).
  - Worst-case: O(n) if the tree is skewed; best-case O(log n) if balanced.

