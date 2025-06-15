# Rotate Image

## Problem Statement

You are given an `n x n` 2D matrix representing an image.  
Rotate the image **by 90 degrees clockwise**, **in-place**.

You must modify the input matrix directly.  
**Do not** allocate another 2D matrix for the rotation.

---

## Examples

### Example 1
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
output = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```
**Explanation:**
The original matrix is rotated 90 degrees clockwise.
The first row becomes the last column, the second row becomes the second last column, and so on.
### Example 2
```python
matrix = [
    [1, 2],
    [3, 4]
]
output = [
    [3, 1],
    [4, 2]
]
```


---

## Constraints

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

## Solution Overview

This solution rotates the matrix in-place by combining two matrix operations:

1. **Transpose the matrix**  
   Swap matrix[i][j] with matrix[j][i] to turn rows into columns.

2. **Reverse each row**  
   After transposing, reversing each row gives the 90-degree clockwise rotation.

This approach avoids using extra space, as required.

---

## Complexity Analysis

- **Time Complexity:** `O(n^2)`  
  Each element is visited twice — once for transpose, once for reversal.

- **Space Complexity:** `O(1)`  
  All operations are done in-place using swaps.
