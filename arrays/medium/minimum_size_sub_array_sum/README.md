# Minimum Size Subarray Sum

## Problem Statement

Given an array of positive integers `nums` and a positive integer `target`,  
return the **minimal length** of a contiguous subarray of which the sum is **greater than or equal to `target`**.  
If no such subarray exists, return `0` instead.

---

## Examples

### Example 1

**Input:**
```python
nums = [2, 3, 1, 2, 4, 3]
target = 7
```
**Output:**
```python
4
```
**Explanation:**
The subarray `[4, 3]` has the minimal length under the problem constraint.

### Example 2
**Input:**
```python
nums = [1, 4, 4]
target = 4
```
**Output:**
```python
4
```
**Explanation:**
The subarray `[4]` has the minimal length under the problem constraint.

### Example 3
**Input:**
```python
nums = [1, 1, 1, 1, 1, 1]
target = 11
```
**Output:**
```python
0
```

**Explanation:**  
No subarray meets the target.

---

## Constraints

- `1 <= target <= 10⁹`
- `1 <= nums.length <= 10⁵`
- `1 <= nums[i] <= 10⁴`

---

## Follow-up

Can you solve it in **O(n)** time using a sliding window?  
Try to implement a second solution with **O(n log n)** time complexity using binary search.

---

## Solution Overview

This solution uses a **variable-size sliding window** to efficiently track the sum of a subarray:

- Two pointers `left` and `right` define the window.
- Expand the window by moving `right` and adding to the running sum.
- Once the sum is greater than or equal to `target`, shrink the window from the left while maintaining the constraint.
- Keep track of the smallest valid window length seen during the traversal.

This technique ensures we only traverse the array once, providing an efficient linear-time solution.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`  
  Each element is added to and removed from the window at most once.

- **Space Complexity:** `O(1)`  
  Constant space is used for tracking sums and window bounds.
