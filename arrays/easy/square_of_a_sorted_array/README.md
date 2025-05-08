# Squares of a Sorted Array

## Problem Statement

Given an integer array `nums` sorted in **non-decreasing order**, return a new array consisting of the **squares of each number**, also sorted in **non-decreasing order**.

---

## Examples

### Example 1

**Input:**
```python
nums = [-4, -1, 0, 3, 10]
```
**Output:**
```python
[0, 1, 9, 16, 100]
```
**Explanation:**
The squares of the numbers are `[16, 1, 0, 9, 100]`, which is sorted in non-decreasing order.

### Example 2
**Input:**
```python
nums = [-7, -3, 2, 3, 11]
```
**Output:**
```python
[4, 9, 9, 49, 121]
```
**Explanation:**
The squares of the numbers are `[49, 9, 4, 9, 121]`, which is sorted in non-decreasing order.


---

## Constraints

- `1 <= nums.length <= 10⁴`
- `-10⁴ <= nums[i] <= 10⁴`
- `nums` is sorted in **non-decreasing order**

---

## Follow-Up

Squaring each element and sorting the array is straightforward and gives an `O(n log n)` solution.  
Can you solve this problem in **O(n)** time using a different approach?
