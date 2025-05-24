# Number of Zero-Filled Subarrays

## Problem Statement

Given an integer array `nums`, return the **number of subarrays filled with `0`**.

A **subarray** is a contiguous non-empty sequence of elements within an array.

---

## Examples

### Example 1
```python
Input: nums = [1, 3, 0, 0, 2, 0, 0, 4]
Output: 6
Explanation: The subarrays filled with `0` are:
[0], [0], [0], [0, 0], [0, 0], [0, 0, 0].
```

### Example 2
```python
Input: nums = [0, 0, 0, 2, 0, 0]
Output: 9
Explanation: The subarrays filled with `0` are:
[0], [0], [0], [0, 0], [0, 0], [0, 0, 0], [0, 0, 0, 2], [0, 0, 2], [0, 2].
```

### Example 3
```python
Input: nums = [1, 2, 3]
Output: 0
```

---

## Constraints

- `1 <= nums.length <= 10⁵`
- `-10⁹ <= nums[i] <= 10⁹`

## Solution Overview

This solution uses a **linear scan** with a **running counter** to count all subarrays that consist entirely of zeros.

### Key Idea:
- For every zero encountered, it can form:
  - A new subarray `[0]`
  - An extended subarray with previous zeros like `[0, 0]`, `[0, 0, 0]`, etc.
- Maintain a counter `count_times` for the current streak of consecutive zeros.
- For each zero, add `1 + count_times` to the total and increment `count_times`.
- Reset `count_times` to 0 on any non-zero.

This ensures **every valid zero-filled subarray is counted once** and avoids redundant calculations.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`  
  - Single pass through the input array

- **Space Complexity:** `O(1)`  
  - Uses only scalar variables for tracking the count
