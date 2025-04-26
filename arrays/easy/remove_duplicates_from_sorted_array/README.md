# Remove Duplicates from Sorted Array

## Problem Statement

Given an integer array `nums` sorted in non-decreasing order,  
remove the duplicates **in-place** such that each unique element appears only once.  
The relative order of the elements should be kept the same.

Return the number of unique elements (`k`),  
and modify the first `k` elements of the array accordingly.

---

## Examples

### Example 1
- Input: nums = [1,1,2]
- Output: 2, nums = [1,2,_]
- Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).

### Example 2
- Input: nums = [0,0,1,1,1,2,2,3,3,4]
- Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
- Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).

### Example 3
- Input: nums = [1,2,3,4,5]
- Output: 5, nums = [1,2,3,4,5]
- Explanation: Your function should return k = 5, with the first five elements of nums being 1, 2, 3, 4, and 5 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).

## Constraints

- 1 <= nums.length <= 3 × 10⁴
- -100 <= nums[i] <= 100
- `nums` is sorted in non-decreasing order.

---

## Solution Overview

This solution uses a **two-pointer approach**:

- One pointer (`i`) traverses the array.
- The second pointer (`idx`) keeps track of the position where the next unique element should be placed.
- When a non-duplicate element is found, it is moved to the `idx` position, and `idx` is incremented.

This method modifies the array **in-place** without allocating extra memory.

---

## Complexity Analysis

- **Time Complexity:** O(n)  
  We iterate through the array once.

- **Space Complexity:** O(1)  
  No additional space is used apart from a few variables.
