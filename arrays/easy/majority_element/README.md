# Majority Element

## Problem Statement

Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.  
You may assume that the majority element **always exists** in the array.

---

## Examples

### Example 1

```python
nums = [3, 2, 3]
```
**Output:** `3`
**Explanation:** The majority element is `3`, which appears 3 times (more than ⌊3 / 2⌋ = 1.5 times).

### Example 2

```python
nums = [2, 2, 1, 1, 1, 2, 2]
```
**Output:** `2`
**Explanation:** The majority element is `2`, which appears 4 times (more than ⌊7 / 2⌋ = 3.5 times).


---

## Constraints

- n == nums.length
- 1 <= n <= 5 × 10⁴
- -10⁹ <= nums[i] <= 10⁹

---

## Follow Up

- Can you solve the problem in **linear time** and in **O(1) space**?

---

## Solution Overview

This solution uses a **Hash Map Frequency Counting** approach:

- Traverse the array and count the frequency of each number using a hash map.
- After counting, find the number with the highest frequency.
- Since the majority element is guaranteed to exist, the maximum frequency element is the answer.

---

### Complexity Analysis

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
