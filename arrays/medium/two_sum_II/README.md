# Two Sum II - Input Array Is Sorted

## Problem Statement

Given a 1-indexed array of integers `numbers` that is sorted in non-decreasing order,  
find two numbers such that they add up to a specific `target` number.

Return the indices of the two numbers, added by one, as an integer array `[index1, index2]` of length 2.

- You must use only constant extra space.
- Exactly one solution exists, and you cannot use the same element twice.

---

## Examples

### Example 1

```python
numbers = [2, 7, 11, 15]
target = 9
```
**Output:** `[1, 2]`
**Explanation:** Because `numbers[0] + numbers[1] == 9`, we return `[1, 2]`.
### Example 2

```python
numbers = [2, 3, 4]
target = 6
```
**Output:** `[1, 3]`
**Explanation:** Because `numbers[0] + numbers[2] == 6`, we return `[1, 3]`.

### Example 3

```python
numbers = [-1, 0]
target = -1
```
**Output:** `[1, 2]`
**Explanation:** Because `numbers[0] + numbers[1] == -1`, we return `[1, 2]`.

## Solution Overview

This solution uses a **Two-Pointer Approach**:

- Initialize two pointers: `left` at the beginning and `right` at the end of the sorted array.
- At each step, check the sum of the two pointers:
  - If the sum is greater than the target, move the right pointer leftward.
  - If the sum is less than the target, move the left pointer rightward.
- Since exactly one solution is guaranteed, the loop always terminates when the correct pair is found.

---

### Complexity Analysis

- **Time Complexity:** O(n)  
  Each element is processed at most once.

- **Space Complexity:** O(1)  
  No extra space is used beyond a few pointers.