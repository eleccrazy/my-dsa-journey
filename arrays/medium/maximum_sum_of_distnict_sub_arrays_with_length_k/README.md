# Maximum Sum of Distinct Subarrays With Length K

## Problem Statement

You are given an integer array `nums` and an integer `k`.

Find the **maximum sum** of all **contiguous subarrays** of length `k` in `nums` that satisfy the following condition:

- All the elements in the subarray must be **distinct**.

Return the **maximum sum** among all valid subarrays.  
If no such subarray exists, return `0`.

---

## Examples

### Example 1

```python
nums = [1, 5, 4, 2, 9, 9, 9]
k = 3
output = 15
```

**Explanation:**

The valid subarrays of length 3 with distinct elements are:
- `[1, 5, 4]` → sum = 10  
- `[5, 4, 2]` → sum = 11  
- `[4, 2, 9]` → sum = 15 ✅  
- `[2, 9, 9]` → ❌ invalid (duplicate 9)  
- `[9, 9, 9]` → ❌ invalid (all elements same)

---

### Example 2

**Input:**
```python
nums = [4, 4, 4]
k = 3
output = 0
```

**Explanation:**  
Only one subarray of length 3: `[4, 4, 4]` → ❌ not valid (repeats).

---

## Constraints

- `1 <= k <= nums.length <= 10⁵`
- `1 <= nums[i] <= 10⁵`

---

## Solution Overview

This solution uses a **sliding window** with a **frequency map** to track distinct elements:

- Start by computing the sum of the first `k` elements and counting their frequencies.
- Slide the window one element at a time:
  - Subtract the element that leaves the window.
  - Add the new element entering the window.
  - Update the frequency map accordingly.
- At each step, check if the number of unique elements equals `k`.
  - If yes, it's a valid subarray; update `max_sum` if the current sum is greater.
- If no valid subarray is found, return 0.

This ensures only subarrays with all distinct elements contribute to the result.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`  
  Each element is added and removed from the frequency map exactly once.

- **Space Complexity:** `O(k)`  
  The frequency map holds at most `k` distinct elements at any time.
