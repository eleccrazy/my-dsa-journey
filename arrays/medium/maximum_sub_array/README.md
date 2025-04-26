# Maximum Subarray

## Problem Statement

Given an integer array `nums`,  
find the contiguous subarray with the largest sum,  
and return its sum.

---

## Examples

### Example 1

- Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
- Output: 6
- Explanation: [4,-1,2,1] has the largest sum = 6.

### Example 2
- Input: nums = [1]
- Output: 1
- Explanation: The subarray [1] has the largest sum = 1.

### Example 3
- Input: nums = [5,4,-1,7,8]
- Output: 23
- Explanation: The subarray [5,4,-1,7,8] has the largest sum = 23.


---

## Constraints

- 1 <= nums.length <= 10⁵
- -10⁴ <= nums[i] <= 10⁴

---

## Solution Overview

## 📈 Solution Overview

This solution uses a **Greedy approach combined with simple dynamic programming ideas**:

- At each index, the algorithm decides:
  - Whether to extend the current subarray by including the current number
  - Or to start a new subarray beginning from the current number
- By making the locally optimal choice at each step, the algorithm ensures that the global maximum subarray sum is found efficiently.
- The running maximum is updated throughout the traversal without using additional space.

> *(This technique is commonly known as Kadane’s Algorithm.)*

---

### Complexity Analysis

- **Time Complexity:** O(n)  
  Single pass through the array.

- **Space Complexity:** O(1)  
  Only constant space is used for variables.

---

