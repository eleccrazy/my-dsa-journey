# Increasing Triplet Subsequence

## Problem Statement

Given an integer array `nums`, return `true` if there exists a triplet of indices `(i, j, k)` such that:

- `i < j < k`
- `nums[i] < nums[j] < nums[k]`

Otherwise, return `false`.

---

## Examples

### Example 1
```python
Input: nums = [1, 2, 3, 4, 5]
Output: true
```
**Explanation:** The triplet `(1, 2, 3)` satisfies the condition.

### Example 2
```python
Input: nums = [5, 4, 3, 2, 1]
Output: false
```
**Explanation:** No triplet exists that satisfies the condition.

### Example 3
```python
Input: nums = [2, 1, 5, 0, 4, 6]
Output: true
```
**Explanation:** The triplet `(1, 5, 6)` satisfies the condition.


---

## Constraints

- `1 <= nums.length <= 5 * 10⁵`
- `-2³¹ <= nums[i] <= 2³¹ - 1`

---

## Follow-Up

Can you implement a solution that runs in **O(n)** time and uses **O(1)** space?

## Solution Overview

This solution uses a **greedy tracking approach** to determine whether an increasing triplet subsequence exists in the input array.

### Key Idea:
Maintain two variables:
- `first`: the smallest number seen so far
- `second`: the smallest number greater than `first`

Iterate through the array:
- If the current number is smaller than or equal to `first`, update `first`
- Else if it’s smaller than or equal to `second`, update `second`
- Else, the current number is larger than both → an increasing triplet exists

By only tracking the two smallest increasing values, this approach detects a valid triplet in a single pass, using constant space.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`  
  - Single pass through the array

