# Permutation in String

## Problem Statement

Given two strings `s1` and `s2`, return `True` if `s2` contains a permutation of `s1`, or `False` otherwise.

In other words, return `True` if one of `s1`'s permutations is a substring of `s2`.

---

## Examples

### Example 1

```python
s1 = "ab"
s2 = "eidbaooo"
output = True
```

### Example 2

```python
s1 = "ab"
s2 = "eidboaoo"
output = False
```

### Example 3

```python
s1 = "abc"
s2 = "ccccbbbbaaaa"
output = False
```

---

## Constraints

- `1 <= s1.length, s2.length <= 10⁴`
- `s1` and `s2` consist of lowercase English letters only

---

## Solution Overview

This solution uses a **sliding window with frequency maps**:

- Create a frequency map (`s1_count`) for characters in `s1`
- Create a second map (`s2_count`) for the first window of size `len(s1)` in `s2`
- Slide the window across `s2`, one character at a time:
  - Add the new character entering the window
  - Remove the character leaving the window
  - At each step, compare the two frequency maps
- If at any point the maps match, a permutation of `s1` exists in `s2`, so return `True`
- If the loop completes with no matches, return `False`

This method avoids recomputing the entire map for each window and leverages the fixed 26-letter alphabet for efficient comparison.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`  
  Where `n` is the length of `s2`. Each character is processed once, and frequency map comparison is constant time.

- **Space Complexity:** `O(1)`  
  Frequency maps are limited to 26 lowercase letters, so space usage is constant.
