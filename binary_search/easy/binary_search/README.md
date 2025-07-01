# Binary Search

## Problem Statement

Given a sorted array of unique integers `nums` and an integer `target`, return the index of `target` if it exists in the array.  
Otherwise, return `-1`.

You **must** implement an algorithm with **O(log n)** runtime complexity.

---

## Examples

### Example 1
Input: `nums = [-1,0,3,5,9,12], target = 9`
Output: `4`
### Example 2
Input: `nums = [-1,0,3,5,9,12], target = 2`
Output: `-1`
### Example 3
Input: `nums = [1], target = 1`
Output: `0`


---

## Constraints

- `1 <= nums.length <= 10⁴`
- `-10⁴ < nums[i], target < 10⁴`
- All integers in `nums` are **unique**
- `nums` is sorted in **ascending order**

## Solution Overview

This solution uses the classic **binary search** technique.

1. Initialize two pointers `left` and `right` to the start and end of the list.
2. While `left <= right`:
   - Compute the midpoint.
   - If the middle element is the target, return its index.
   - If the target is smaller, discard the right half.
   - If the target is larger, discard the left half.
3. If the loop exits, the target is not in the list; return -1.

---

## Complexity Analysis

- **Time Complexity:** `O(log n)`
  - Each iteration reduces the search space by half.

- **Space Complexity:** `O(1)`
  - Uses only constant space for pointers.

