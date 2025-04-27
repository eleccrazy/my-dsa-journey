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

The current solution appends elements from `nums2` into `nums1` at the appropriate positions,  
then sorts the merged array to achieve the correct final ordering.

This approach leverages Python's in-place `.sort()` method.

---

### Complexity Analysis

- **Time Complexity:** O((m + n) log(m + n))  
- **Space Complexity:** O(1) (in-place)


