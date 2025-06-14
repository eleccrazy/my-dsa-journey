# Spiral Matrix

## Problem Statement

Given an `m x n` matrix, return **all elements of the matrix in spiral order**.

You must traverse the matrix in the following order:
- Left to right
- Top to bottom
- Right to left
- Bottom to top

Repeat this pattern while narrowing the boundaries.

---

## Examples

### Example 1
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
output = [1, 2, 3, 6, 9, 8, 7, 4, 5]
```
**Explanation:**
The spiral order starts from the top-left corner, moves right across the first row, then down the last column, left across the last row, and finally up the first column, repeating this process until all elements are visited.
### Example 2
```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
output = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
```


---

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

## Solution Overview

The solution uses a **boundary-tracking approach** to simulate spiral movement.

- It starts with `top`, `bottom`, `left`, and `right` pointers.
- It iteratively traverses in the order: right → down → left → up.
- After each directional traversal, the corresponding boundary is updated inward.
- The loop continues until all `m * n` elements have been collected.

This approach ensures each element is visited exactly once, making it both efficient and intuitive.

---

## Complexity Analysis

- **Time Complexity:** `O(m * n)`  
  Each element in the matrix is visited once.

- **Space Complexity:** `O(1)` extra  
  Aside from the result list, no additional space is used.

