# Find the Index of the First Occurrence in a String

## Problem Statement

Given two strings `haystack` and `needle`,  
return the index of the first occurrence of `needle` in `haystack`,  
or `-1` if `needle` is not part of `haystack`.

---

## Examples

### Example 1

```python
haystack = "sadbutsad"
needle = "sad"
```
**Output:** `0`
**Explanation:** The substring "sad" occurs at index 0 and 6. The first occurrence is at index 0, so we return 0.

### Example 2

```python
haystack = "leetcode"
needle = "leeto"
```
**Output:** `-1`
**Explanation:** The substring "leeto" is not present in "leetcode", so we return -1.

### Example 3

```python
haystack = "a"
needle = "a"
```
**Output:** `0`
**Explanation:** The substring "a" occurs at index 0. The first occurrence is at index 0, so we return 0.

## Constraints

- 1 <= haystack.length, needle.length <= 10⁴
- `haystack` and `needle` consist of only lowercase English characters.

---

## Solution Overview

This solution uses a **Two-Pointer Sliding Window** approach:

- A window of size equal to the `needle` is moved across `haystack`.
- At each position, the substring is compared to `needle`.
- The first matching position is returned; if no match, return -1.

---

### Complexity Analysis

- **Time Complexity:** O((n - m + 1) * m)
- **Space Complexity:** O(1)
