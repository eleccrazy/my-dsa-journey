# Contains Duplicate

## Problem Statement

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array,  
and return `false` if every element is **distinct**.

---

## Examples

### Example 1  
Input: `nums = [1,2,3,1]`  
Output: `true`  
Explanation: The element `1` occurs at the indices 0 and 3.

### Example 2  
Input: `nums = [1,2,3,4]`  
Output: `false`  
Explanation: All elements are distinct.

### Example 3  
Input: `nums = [1,1,1,3,3,4,3,2,4,2]`  
Output: `true`

---

## Constraints

- `1 <= nums.length <= 10⁵`
- `-10⁹ <= nums[i] <= 10⁹`

---

## Solution Overview

Solve Contains Duplicate by comparing set size to original list size

- Convert the list to a set, which removes duplicates
- If the set length is smaller, at least one duplicate exists
- Return `True` if duplicates found, else `False`

## Complexity Analysis

- **Time Complexity:** `O(n)`  
  Creating a set from `n` elements requires linear time.

- **Space Complexity:** `O(n)`  
  A set of up to `n` elements is created in the worst case.
