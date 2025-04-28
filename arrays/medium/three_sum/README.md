# 3Sum

## Problem Statement

Given an integer array `nums`,  
return all the triplets `[nums[i], nums[j], nums[k]]` such that:

- `i != j`, `i != k`, and `j != k`
- `nums[i] + nums[j] + nums[k] == 0`

The solution set must not contain duplicate triplets.

---

## Examples

### Example 1

```python
nums = [-1, 0, 1, 2, -1, -4]
```
**Output:** `[[-1, -1, 2], [-1, 0, 1]]`
**Explanation:** The triplets `[-1, -1, 2]` and `[-1, 0, 1]` sum to zero.

### Example 2

```python
nums = []
```
**Output:** `[]`

**Explanation:** There are no triplets in an empty array.
### Example 3

```python
nums = [0]
```
**Output:** `[]`

**Explanation:** There are no triplets in an array with a single element.
### Example 4

```python
nums = [0, 0, 0]
```
**Output:** `[[0, 0, 0]]`
**Explanation:** The triplet `[0, 0, 0]` sums to zero.

## Solution Overview

This solution uses a **Sorting + Two-Pointer Approach**:

- Sort the input array to enable efficient two-pointer scanning.
- For each element, treat it as a fixed number and find two other numbers using two pointers (`left` and `right`) that sum up to the negative of the fixed number.
- Skip duplicate elements to avoid returning duplicate triplets.
- Continue until all unique triplets summing to zero are found.

---

### Complexity Analysis

- **Time Complexity:** O(n²)
- **Space Complexity:** O(1) (ignoring output list size)
