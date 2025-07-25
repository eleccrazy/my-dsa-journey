# Search Insert Position

## Problem Statement

Given a **sorted array** of **distinct integers** and a target value, return the **index** if the target is found.  
If not, return the index **where it would be if it were inserted** in order.

You **must** write an algorithm with **O(log n)** runtime complexity.

---

## Examples

### Example 1  
Input: `nums = [1,3,5,6]`, `target = 5`  
Output: `2`

### Example 2  
Input: `nums = [1,3,5,6]`, `target = 2`  
Output: `1`

### Example 3  
Input: `nums = [1,3,5,6]`, `target = 7`  
Output: `4`

---

## Constraints

- `1 <= nums.length <= 10⁴`
- `-10⁴ <= nums[i] <= 10⁴`
- `nums` contains **distinct values** sorted in **ascending order**
- `-10⁴ <= target <= 10⁴`

## Solution Overview

Solve Search Insert Position using binary search

- Standard binary search to locate `target` or insertion point
- Maintain two pointers: `left` and `right`
- If `target` not found, return `left` as the correct insert index

---

## Complexity Analysis

- **Time Complexity:** `O(log n)`  
  Binary search halves the search space each iteration.

- **Space Complexity:** `O(1)`  
  Constant space is used for pointer tracking.
