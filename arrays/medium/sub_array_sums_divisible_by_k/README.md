# Subarray Sums Divisible by K

## Problem Statement

Given an integer array `nums` and an integer `k`,  
return the **number of non-empty subarrays** that have a sum **divisible by `k`**.

A subarray is a contiguous part of an array.

---

## Examples

### Example 1

**Input:**
```python
nums = [4, 5, 0, -2, -3, 1]
k = 5
```
**Output:**
```python
7
```

**Explanation:**  
The following 7 subarrays have sums divisible by 5:
- [4, 5, 0, -2, -3, 1]
- [5]
- [5, 0]
- [5, 0, -2, -3]
- [0]
- [0, -2, -3]
- [-2, -3]

---

### Example 2

**Input:**
```python
nums = [5]
k = 9
```
**Output:**
```python
0
```

---

## Constraints

- `1 <= nums.length <= 3 * 10⁴`
- `-10⁴ <= nums[i] <= 10⁴`
- `2 <= k <= 10⁴`

---

## Solution Overview

This problem uses **prefix sums combined with modulo arithmetic**.

- Maintain a running sum `current_sum` while traversing the array.
- Compute the **remainder** of `current_sum % k`.
- If the same remainder has been seen before, it means a subarray between those two indices has a sum divisible by `k`.
- Use a hashmap `prefix_sum` to track how often each remainder has appeared.
- Initialize `prefix_sum[0] = 1` to count subarrays that start at index 0.
```


---

## Complexity Analysis

- **Time Complexity:** `O(n)`  
  Single pass through the array with constant-time hashmap operations.

- **Space Complexity:** `O(k)`  
  At most `k` unique remainders stored in the hashmap.
