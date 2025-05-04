# Maximum Average Subarray I

## Problem Statement

You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a contiguous subarray of length `k` that has the **maximum average value**, and return this value.  
Any answer with a **calculation error less than 10⁻⁵** will be accepted.

---

## Examples

### Example 1

```python
nums = [1,12,-5,-6,50,3]
k = 4
output = 12.75000
```

### Example 2

```python
nums = [5,5,5,5]
k = 1
output = 5.00000
```

### Example 3

```python
nums = [1,2,3,4,5]
k = 2
output = 4.00000
```

## Constraints
- `n == nums.length`
- `1 <= k <= n <= 10⁵`
- `-10⁴ <= nums[i] <= 10⁴`

---

## Solution Overview

This solution uses a **sliding window with a running sum**:

- Start by computing the sum of the first `k` elements.
- Then slide the window one step at a time:
  - Subtract the element that is leaving the window.
  - Add the element that is entering the window.
- Keep track of the maximum sum seen so far.
- At the end, divide the maximum sum by `k` to get the maximum average.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`  
  The array is traversed once, and each update to the sum is constant time.

- **Space Complexity:** `O(1)`  
  Only a few variables are used; no extra data structures are needed.
