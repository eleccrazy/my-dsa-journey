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

---
## Solution Approach
1. **Two Pointers Approach**: 
   - Initialize two pointers, `left` at the start of the array and `right` at the end.
   - Compare the absolute values of the elements at these pointers.
   - Square the larger absolute value and place it in the result array from the end towards the start.
   - Move the pointer of the larger absolute value inward.
   - Continue until all elements are processed.
2. **Result Array**:
    - Initialize a result array of the same length as `nums`.
    - Fill it with squares of the elements in sorted order.
3. **Return the Result**:
    - Return the result array.

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array `nums`. We traverse the array once.
- **Space Complexity**: `O(n)`, for the result array. The input array is not modified.
- **In-place**: The algorithm does not modify the input array, but it uses additional space for the result array.