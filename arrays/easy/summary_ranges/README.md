# Summary Ranges

## Problem Statement

You are given a **sorted**, **unique** integer array `nums`.

A range `[a, b]` is the set of all integers from `a` to `b` (inclusive).

Return the **smallest sorted list of ranges** that:
- Cover all elements in `nums`
- Each number is covered by exactly one range
- No integer appears outside of the defined ranges

Each range `[a, b]` should be formatted as:
- `"a->b"` if `a != b`
- `"a"` if `a == b`

---

## Examples

### Example 1
```python
Input: nums = [0, 1, 2, 4, 5, 7]
Output: ["0->2", "4->5", "7"]
```
### Example 2
```python
Input: nums = [0, 2, 3, 4, 6, 8, 9]
Output: ["0", "2->4", "6", "8->9"]
```
### Example 3
```python
Input: nums = []
Output: []
```

