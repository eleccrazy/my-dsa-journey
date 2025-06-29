# Baseball Game

## Problem Statement

You are keeping scores for a baseball game with unusual rules.  
You're given a list of operations, where each operation modifies a running list of scores:

- An integer `x`: Record `x` as a new score.
- `"+"`: Record the sum of the **previous two** scores.
- `"D"`: Record **double** the previous score.
- `"C"`: Invalidate and **remove** the previous score.

Return the **sum of all scores** after performing all operations.

All operations are guaranteed to be valid.

---

## Examples

### Example 1
```python
scores = ["5", "2", "C", "D", "+"]
# Output: 30
# Explanation:
# - Record 5: scores = [5]
# - Record 2: scores = [5, 2]
# - Invalidate last score: scores = [5]
# - Record double last score: scores = [5, 10]
# - Record sum of last two scores: scores = [5, 10, 15]
# - Final sum: 5 + 10 + 15 = 30
```
### Example 2
```python
scores = ["5", "-2", "4", "C", "D", "9", "+"]
# Output: 27
# Explanation:
# - Record 5: scores = [5]
# - Record -2: scores = [5, -2]
# - Record 4: scores = [5, -2, 4]
# - Invalidate last score: scores = [5, -2]
# - Record double last score: scores = [5, -2, -4]
# - Record sum of last two scores: scores = [5, -2, -4, 1]
# - Final sum: 5 + -2 + -4 + 1 = 27
```
### Example 3
```python
scores = ["1", "C"]
# Output: 0
# Explanation:
# - Record 1: scores = [1]
# - Invalidate last score: scores = []
# - Final sum: 0
```

---

## Constraints

- `1 <= operations.length <= 1000`
- Each operation is `"C"`, `"D"`, `"+"`, or a string integer in `[-30,000, 30,000]`
- For `"+"`, there are always at least 2 previous scores
- For `"D"` and `"C"`, there is always at least 1 previous score

## Solution Overview

We simulate the baseball game's scoring rules using a stack (`record`) to keep track of valid scores:

- For an integer value: convert and append it.
- `"+"`: Add the sum of the last two scores.
- `"D"`: Double the last score.
- `"C"`: Remove the most recent score.

This approach ensures all operations are valid and efficiently processed.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
  - Each operation is processed exactly once.
- **Space Complexity:** `O(n)`
  - Stores scores from valid operations.

