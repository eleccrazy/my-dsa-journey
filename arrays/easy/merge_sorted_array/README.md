# Merge Sorted Array

## Problem Statement

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order,  
and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums2` into `nums1` so that the resulting array is sorted in non-decreasing order.

The merged result must be stored inside `nums1` in-place, without using extra space for another array.

---

## Examples

### Example 1

Input:
```python
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m = 3
n = 3
```
Output:
```python
[1, 2, 2, 3, 5, 6]
```
### Example 2
Input:
```python
nums1 = [1]
nums2 = []
m = 1
n = 0
```

---

## Constraints

- `nums1.length == m + n`
- `nums2.length == n`
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -10⁹ <= nums1[i], nums2[j] <= 10⁹

---

## Solution Overview

This problem was solved using two approaches:

1. **Simple Approach (Copy + Sort)**  
   - Copy elements from `nums2` into `nums1` after the initial `m` elements.
   - Sort the combined array using Python’s in-place `.sort()` method.
   
2. **Optimized Approach (Two Pointers, In-Place Merge)**  
   - Start two pointers at the end of the valid parts of `nums1` and `nums2`.
   - Compare elements from the back and place the larger one at the end of `nums1`.
   - Move the pointers backward accordingly.
   - If any elements remain in `nums2`, copy them into the beginning of `nums1`.

Both approaches ensure that the final array is sorted and stored in `nums1` as required.

---

### Complexity Analysis

- **Simple Approach (Copy + Sort):**
  - **Time Complexity:** O((m + n) log(m + n))
  - **Space Complexity:** O(1) (in-place)

- **Optimized Approach (Two Pointers):**
  - **Time Complexity:** O(m + n)
  - **Space Complexity:** O(1) (in-place)