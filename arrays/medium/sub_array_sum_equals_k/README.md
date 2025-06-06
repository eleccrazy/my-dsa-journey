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

---

## Solution Overview

This problem is solved using **prefix sums with a hashmap**:

- Track the running `current_sum` as we iterate through the array.
- For each element, compute the difference `current_sum - k`. If this difference has been seen before, it means there is a subarray ending at the current index that sums to `k`.
- Use a hashmap (`prefixCount`) to store the number of times each cumulative sum has occurred so far.
- Initialize with `{0: 1}` to account for subarrays that start at index 0.

This allows us to find all subarrays summing to `k` in a single pass.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`  
  Each element is visited once, and hashmap operations are O(1).

- **Space Complexity:** `O(n)`  
  Stores up to `n` prefix sums in the hashmap.
