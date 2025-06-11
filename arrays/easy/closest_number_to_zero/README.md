# Find Closest Number to Zero

## Problem Statement

Given an integer array `nums` of size `n`, return the number with the value **closest to 0** in the array.  
If there are **multiple answers**, return the number with the **larger value**.

---

## Examples

### Example 1
```python
nums = [-4, -2, 1, 4, 8]
```
**Output:** `1`
**Explanation:** The closest number to 0 is `1`.
### Example 2
```python
nums = [2, -1, 3, -4]
```
**Output:** `-1`
**Explanation:** The closest number to 0 is `-1`, which is larger than `-4`.
### Example 3
```python
nums = [0, 0, 0]
```
**Output:** `0`


---

## Constraints

- `1 <= n <= 1000`
- `-10⁵ <= nums[i] <= 10⁵`

## Solution Overview

This solution finds the integer in the array that is **closest to 0** by iterating through the list and comparing the absolute values of each number.

- Initialize `min_dist` with the absolute value of the first number.
- As you iterate, if a number has a smaller absolute value, update `min_dist` and track that number.
- If two numbers are equally close to zero, select the **larger one**.
- Return the number with the smallest absolute distance to zero (breaking ties in favor of the larger number).

This approach ensures correctness with a single linear scan.

## Complexity Analysis

- **Time Complexity:** `O(n)`
  - One pass through the array

- **Space Complexity:** `O(1)`
  - Uses only a few variables to track state
