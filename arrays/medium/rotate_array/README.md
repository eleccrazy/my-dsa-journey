# Rotate Array

## Problem Statement

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

Each rotation shifts all elements to the right by 1, wrapping the last element to the front.

---

## Examples

### Example 1

```python
nums = [1,2,3,4,5,6,7]
k = 3
output = [5,6,7,1,2,3,4]
```

### Example 2

```python
nums = [-1,-100,3,99]
k = 2
output = [3,99,-1,-100]
```

### Example 3

```python
nums = [1,2]
k = 1
output = [2,1]
```

## Constraints
- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

---

## Solution Overview

This solution uses **Python slicing** to rotate the array:

- First, calculate `k % n` to handle cases where `k` is larger than the array size.
- Then, split the array into two parts:
  - The last `k` elements: `nums[-k:]`
  - The first `n-k` elements: `nums[:-k]`
- Concatenate them to get the rotated array and reassign it in-place with `nums[:]`.

This is a very concise and readable approach in Python but uses extra space.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`  
  Slicing and concatenation each take linear time.

- **Space Complexity:** `O(n)`  
  A new list is created during slicing, so this is not an in-place rotation.
