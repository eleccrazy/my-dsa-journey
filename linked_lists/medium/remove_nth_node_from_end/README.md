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
