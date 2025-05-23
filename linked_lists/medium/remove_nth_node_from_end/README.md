# Remove Nth Node From End of List

## Problem Statement

Given the `head` of a linked list, remove the `n`th node from the **end** of the list and return its head.

---

## Examples

### Example 1
```python
Input
[1, 2, 3, 4, 5], n = 2
Output
[1, 2, 3, 5]
```
### Example 2
```python
Input
[1], n = 1
Output
[]
```
### Example 3
```python
Input
[1, 2], n = 1
Output
[1]
```

---

## Constraints

- The number of nodes in the list is `sz`
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

---

## Follow-up

Can you solve this problem in **one pass**?

## Solution Overview

This solution uses a **two-pointer technique with a dummy node** to remove the `n`th node from the end of a singly linked list in one pass.

### Steps:
1. Create a dummy node that points to the head of the list to simplify edge case handling.
2. Initialize two pointers (`left` and `right`) at the dummy node.
3. Move the `right` pointer `n + 1` steps ahead to create a gap of `n` nodes between the two pointers.
4. Move both pointers together until `right` reaches the end.
5. The `left` pointer now points to the node before the one that needs to be removed.
6. Adjust `left.next` to skip the target node and unlink it from the list.

This approach ensures only **one traversal** of the list is needed and avoids computing its length beforehand.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`  
  - Each node is visited at most once.

- **Space Complexity:** `O(1)`  
  - Only a constant amount of extra space is used (no additional data structures).
