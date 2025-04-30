# Longest Common Prefix

## Problem Statement

Write a function to find the **longest common prefix** string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

A common prefix is a substring that is present at the **beginning of every string** in the list.

---

## Examples

### Example 1

```python
Input: strs = ["flower","flow","flight"]
Output: "fl"
```
### Example 2

```python
Input: strs = ["dog","racecar","car"]
Output: ""
```
### Example 3

```python
Input: strs = ["a"]
Output: "a"
```

---

## Constraints

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists only of lowercase English letters (if not empty)

---

## Solution Overview

This solution uses a **Character-by-Character Comparison** (Two-Pointer/Scan-based approach):

- Determine the length of the shortest string in the list.
- For each index `i` up to that length:
  - Compare the character `strs[0][i]` with the character at the same index in all other strings.
  - If all match, append the character to the prefix.
  - If any mismatch is found, stop and return the prefix up to that point.
- If no mismatch is found, return the entire prefix of length equal to the shortest string.

---

## Complexity Analysis

- **Time Complexity:** `O(n * m)`  
  Where `n` is the number of strings and `m` is the length of the shortest string.

- **Space Complexity:** `O(1)`  
  Only constant space is used beyond the result string.


