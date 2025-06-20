# Invert Binary Tree

## Problem Statement

Given the `root` of a binary tree, invert the tree, and return its root.

Inversion means swapping the left and right children of every node in the tree.

---

## Examples

### Example 1
```python
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```
**Explanation:**
The original tree is:
```
    4
   / \
  2   7
 / \ / \
1  3 6  9
```
After inversion, the tree becomes:
```
    4
   / \
  7   2
 / \ / \
9  6 3  1
```

### Example 2
```python
Input: root = [2,1,3]
Output: [2,3,1]
```


---

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Solution Overview

This recursive solution traverses the binary tree and swaps the left and right children of each node in-place.

- The recursion follows a depth-first traversal.
- At each node, the left and right subtrees are swapped.
- The function continues recursively until all nodes are processed.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
  - Each node is visited once.

- **Space Complexity:** `O(h)`
  - Where `h` is the height of the tree due to recursion.
  - Worst case: `O(n)` (unbalanced tree), Best case: `O(log n)` (balanced).

