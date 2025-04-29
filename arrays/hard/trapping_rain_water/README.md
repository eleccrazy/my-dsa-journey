# Trapping Rain Water

## Problem Statement

You are given an integer array `height` of length `n`,  
where each element represents the elevation of a bar, and the width of each bar is 1.

Compute how much water can be trapped between the bars after it rains.

Return the total amount of trapped rain water.

---

## Examples

### Example 1

```python
height = [0,1,0,2,1,0,1,3,2,1,2,1]
```
**Output:** `6`
**Explanation:** The water can be trapped between the bars at indices `2` and `3`,
`3` and `4`, `4` and `5`, `5` and `6`, and `6` and `7`, resulting in a total of `6` units of water trapped.
**Note:** The water trapped at index `2` is `1` unit, at index `3` is `0` units, at index `4` is `1` unit,
at index `5` is `2` units, at index `6` is `1` unit, and at index `7` is `0` units.

### Example 2

```python
height = [4,2,0,3,2,5]
```
**Output:** `9`
**Explanation:** The water can be trapped between the bars at indices `1` and `2`,
`2` and `3`, `3` and `4`, and `4` and `5`, resulting in a total of `9` units of water trapped.
**Note:** The water trapped at index `1` is `2` units, at index `2` is `0` units,
at index `3` is `3` units, at index `4` is `2` units, and at index `5` is `0` units.

### Example 3

```python
height = [1,0,2]
```
**Output:** `1`
**Explanation:** The water can be trapped between the bars at indices `0` and `1`,
`1` and `2`, resulting in a total of `1` unit of water trapped.
**Note:** The water trapped at index `0` is `0` units, at index `1` is `1` unit, and at index `2` is `0` units.

## Constraints

- `n == height.length`
- `1 <= n <= 2 * 10⁴`
- `0 <= height[i] <= 10⁵`

## Solution Overview

This solution uses a **Prefix Maximum Arrays Approach**:

- Compute a `left_max` array where `left_max[i]` represents the maximum height to the left of or at index `i`.
- Compute a `right_max` array where `right_max[i]` represents the maximum height to the right of or at index `i`.
- For each index `i`, the water that can be trapped above it is the minimum of `left_max[i]` and `right_max[i]` minus the current height.
- Accumulate this value for all indices to compute the total trapped water.

This method ensures that we account for the tallest boundaries on both sides before calculating trapped water, which is crucial for accurate results.

---

### Complexity Analysis

- **Time Complexity:** O(n)  
  Three passes through the array: one for `left_max`, one for `right_max`, and one for calculating the result.

- **Space Complexity:** O(n)  
  Two additional arrays of size `n` are used to store the left and right max heights.
