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

---

## Constraints

- `0 <= nums.length <= 20`
- `-2³¹ <= nums[i] <= 2³¹ - 1`
- All values in `nums` are unique and sorted in **ascending** order.


## Solution Overview

This solution tracks ranges in a sorted list by using a sliding window approach.

- A `start` pointer is used to mark the beginning of a range.
- The loop continues until it finds a break in the consecutive numbers.
- When a break is found (i.e., the current number + 1 ≠ next number), the range is closed and added to the result.
- The final number or range is handled after the loop.

This efficiently identifies all continuous number segments and formats them accordingly.

## Complexity Analysis

- **Time Complexity:** `O(n)`
  - Single pass through the list of numbers

- **Space Complexity:** `O(1)` (excluding output list)
  - Uses a few pointers and counters; result list grows with input
