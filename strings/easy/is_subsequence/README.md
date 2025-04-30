# Is Subsequence

## Problem Statement

Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise.

A **subsequence** of a string is a new string formed from the original string by deleting some (or no) characters without changing the relative order of the remaining characters.

---

## Examples

### Example 1

``` python
Input: s = "abc", t = "ahbgdc"
Output: true
```
### Example 2

``` python
Input: s = "axc", t = "ahbgdc"
Output: false
```
### Example 3

``` python
Input: s = "", t = "ahbgdc"
Output: true
```
---

## Constraints

- `0 <= s.length <= 100`
- `0 <= t.length <= 10⁴`
- `s` and `t` consist only of lowercase English letters

---

## Solution Overview

This solution uses a **Greedy Linear Scan**:

- Initialize a pointer `start` to track where to begin scanning `t`.
- For each character `ch` in `s`, scan `t` from the current `start` position.
- If a match is found, update `start` to the index after the match and continue.
- If no match is found for any character in `s`, return `False`.
- If all characters in `s` are matched in order, return `True`.

This approach maintains the relative order of characters and ensures each character in `s` appears in `t` in sequence.

---

### Complexity Analysis

- **Time Complexity:** O(n * m) in the worst case, where `n = len(s)` and `m = len(t)`  
  For each character in `s`, we may scan the remainder of `t`.

- **Space Complexity:** O(1)  
  Only a few variables are used; no extra data structures are created.
## Solution Overview (Two-Pointer Approach)

This solution uses a **Two-Pointer Technique**:

- Initialize two pointers `i` and `j` at the start of strings `s` and `t`, respectively.
- Move `j` through `t`, and advance `i` only when `s[i] == t[j]`.
- If the `i` pointer reaches the end of `s`, it means all characters of `s` appeared in `t` in order.
- Return `True` if all characters in `s` have been matched; otherwise, return `False`.

This method improves performance by avoiding nested loops and ensures a linear scan through both strings.

---

### Complexity Analysis

- **Time Complexity:** O(n + m)  
  Where `n = len(s)` and `m = len(t)` — each character in both strings is visited at most once.

- **Space Complexity:** O(1)  
  Only constant extra space is used for two pointers.