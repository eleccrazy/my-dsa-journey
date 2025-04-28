# Move Zeroes

## Problem Statement

Given an integer array `nums`,  
move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

- You must do this **in-place** without making a copy of the array.

---

## Examples

### Example 1

```python
nums = [0, 1, 0, 3, 12]
```
**Output:** `[1, 3, 12, 0, 0]`
**Explanation:** The non-zero elements `1`, `3`, and `12` are moved to the front, while the zeros are moved to the end.
**Note:** The order of the non-zero elements is maintained.

### Example 2

```python
nums = [0]
```
**Output:** `[0]`
**Explanation:** The array contains only one element which is `0`, so no changes are needed.
**Note:** The order of the non-zero elements is maintained.

### Example 3

```python
nums = [1, 2, 3]
```
**Output:** `[1, 2, 3]`
**Explanation:** The array contains no zeros, so no changes are needed.
**Note:** The order of the non-zero elements is maintained.


---

## Constraints

- 1 <= nums.length <= 10⁴
- -2³¹ <= nums[i] <= 2³¹ - 1

---

## Follow Up

- Can you minimize the total number of operations done?

---

## Solution Overview

This solution uses a **Two-Pointer Approach**:

- Use two pointers (`left` and `right`) to find and swap zeros and non-zero elements in-place.
- `left` tracks the position where a zero is located.
- `right` moves ahead to find a non-zero element to swap with the zero.
- The relative order of non-zero elements is preserved.

---

### Complexity Analysis

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
