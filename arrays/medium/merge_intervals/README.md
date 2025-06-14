# Merge Intervals

## Problem Statement

You are given an array of intervals where `intervals[i] = [starti, endi]`.  
Your task is to merge all **overlapping intervals**, and return an array of the **non-overlapping intervals** that cover all the intervals in the input.

Two intervals `[a, b]` and `[c, d]` are considered **overlapping** if `c <= b`.

---

## Examples

### Example 1
```python
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
output = [[1, 6], [8, 10], [15, 18]]
```
**Explanation:**
The intervals `[1, 3]` and `[2, 6]` overlap, so they are merged into `[1, 6]`.
The intervals `[8, 10]` and `[15, 18]` do not overlap with any others, so they remain unchanged.
### Example 2
```python
intervals = [[1, 4], [4, 5]]
output = [[1, 5]]
```
**Explanation:**
The intervals `[1, 4]` and `[4, 5]` overlap at the endpoint `4`, so they are merged into `[1, 5]`.


---

## Constraints

- `1 <= intervals.length <= 10⁴`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 10⁴`

