# Max Consecutive Ones III

## Problem Statement

You are given a binary array `nums` and an integer `k`.

Return the **maximum number of consecutive 1's** in the array if you can **flip at most `k` 0's** to 1's.

---

## Examples

### Example 1

**Input:**
```python
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
```
**Output:**
```python
6
```
**Explanation:**  
Flip the two 0's at indices 3 and 4 to get:  
`[1,1,1,1,1,1,1,1,1,1,0]` → the subarray of length 6 from index 5 to 10.

### Example 2
**Input:**
```python
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
```
**Output:**
```python
10
```
**Explanation:**  
Flip 0's at indices 4, 5, and 9 to get a subarray of 10 consecutive 1's.

---

## Constraints

- `1 <= nums.length <= 10⁵`
- `nums[i]` is either `0` or `1`
- `0 <= k <= nums.length`

---

## Solution Overview

This solution uses a **variable-size sliding window**:

- Expand the window using a `right` pointer.
- Count the number of 1s within the window (`one_count`).
- If the window contains more than `k` zeros (i.e., `window_size - one_count > k`), shrink the window from the left.
- At each step, track the maximum valid window size.

This efficiently finds the longest sequence of 1s that can be formed by flipping at most `k` 0s.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`  
  Each element is visited at most twice — once by `right`, once by `left`.

- **Space Complexity:** `O(1)`  
  Only integer counters and pointers are used.

