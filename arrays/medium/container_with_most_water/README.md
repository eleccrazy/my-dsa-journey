# Container With Most Water

## Problem Statement

You are given an integer array `height` of length `n`.  
There are `n` vertical lines drawn such that the two endpoints of the `i`-th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container,  
such that the container holds the most water.

Return the maximum amount of water a container can store.

- The container must be vertical (you cannot slant it).

---

## Examples

### Example 1

```python
height = [1,8,6,2,5,4,8,3,7]
```
**Output:** `49`
**Explanation:** The container formed by lines at indices `1` and `8` (height `8` and `7`) holds the most water, which is `7 * 7 = 49`.

**Note:** The width of the container is `8 - 1 = 7` and the height is `min(8, 7) = 7`, so the area is `7 * 7 = 49`.
### Example 2

```python
height = [1,1]
```
**Output:** `1`
**Explanation:** The container formed by lines at indices `0` and `1` (height `1` and `1`) holds the most water, which is `1 * 1 = 1`.
**Note:** The width of the container is `1 - 0 = 1` and the height is `min(1, 1) = 1`, so the area is `1 * 1 = 1`.

## Constraints

- n == height.length
- 2 <= n <= 10⁵
- 0 <= height[i] <= 10⁴

## Solution Overview

This solution uses a **Two-Pointer Greedy Approach**:

- Initialize two pointers, `left` at the beginning and `right` at the end of the array.
- At each step, calculate the area formed by the lines at `left` and `right`.
- Move the pointer pointing to the shorter line inward, trying to find a taller line to maximize area.
- Continue until the two pointers meet, keeping track of the maximum area found.

This method ensures an O(n) time complexity by considering only necessary comparisons.

---

### Complexity Analysis

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
