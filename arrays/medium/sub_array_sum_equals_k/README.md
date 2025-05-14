# Subarray Sum Equals K

## Problem Statement

Given an array of integers `nums` and an integer `k`,  
return the **total number of continuous subarrays** whose **sum equals `k`**.

A subarray is a contiguous, non-empty sequence of elements within an array.

---

## Examples

### Example 1

**Input:**
```python
nums = [1, 1, 1]
k = 2
```
**Output:**
```python
2
```
**Explanation:**
The subarrays are `[1, 1]` (from index 0 to 1) and `[1, 1]` (from index 1 to 2).
```
### Example 2
**Input:**
```python
nums = [1, 2, 3]
k = 3
```
**Output:**
```python
2
```
**Explanation:**
The subarrays are `[1, 2]` (from index 0 to 1) and `[3]` (from index 2 to 2).
```
---

## Constraints

- `1 <= nums.length <= 2 * 10⁴`
- `-1000 <= nums[i] <= 1000`
- `-10⁷ <= k <= 10⁷`