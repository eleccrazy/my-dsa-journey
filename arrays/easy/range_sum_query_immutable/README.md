# Range Sum Query - Immutable

## Problem Statement

Given an integer array `nums`, implement a class `NumArray` that supports the following operation efficiently:

- `sumRange(left, right)` — returns the sum of elements from index `left` to `right` (inclusive).

You may assume that multiple queries will be made, so optimize for repeated calls.

---

## Example

### Input
```python
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
```
### Output
```python
[null, 1, -1, -3]
```
### Explanation
```python
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
```

---

## Constraints

- `1 <= nums.length <= 10⁴`
- `-10⁵ <= nums[i] <= 10⁵`
- `0 <= left <= right < nums.length`
- Up to `10⁴` calls to `sumRange(...)` may be made

---

## Follow-Up

Can you preprocess the array so that each call to `sumRange` runs in O(1) time?

---

## Solution Overview

This problem is solved using the **prefix sum technique**.

- During initialization, we compute the running cumulative sum of the array and store it as `prefixSum[i] = nums[0] + nums[1] + ... + nums[i]`.
- To get the sum of any subarray from `left` to `right`, we compute:
```python
sumRange(left, right) = prefixSum[right] - prefixSum[left - 1]
```
If `left == 0`, we directly return `prefixSum[right]`.

This makes every `sumRange` call run in constant time.

---

## Complexity Analysis

- **Time Complexity:**
- `__init__`: O(n) — for building the prefix sum array
- `sumRange`: O(1) — constant time for range sum queries

- **Space Complexity:** O(1) (in-place modification of the input list)
