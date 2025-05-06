# Find All Anagrams in a String

## Problem Statement

Given two strings `s` and `p`, return an array of all the **start indices** of `p`'s anagrams in `s`.  
You may return the answer in any order.

An anagram is a rearrangement of letters — for two strings to be anagrams, they must have:
- The same length
- The same character frequency counts

---

## Examples

### Example 1

```python
s = "cbaebabacd"
p = "abc"
output = [0, 6]
```

### Example 2

```python
s = "abab"
p = "ab"
output = [0, 1, 2]
```

### Example 3

```python
s = "aaaaaaaaaa"
p = "aaaaaaaaaaaaa"
output = []
```

## Constraints

- `1 <= s.length, p.length <= 10^4`
- `s` and `p` consist of lowercase English letters.

---

## Solution Overview

This solution uses a **sliding window** and **frequency dictionaries**:

- Count the frequency of characters in `p` once (`p_count`).
- Slide a window of size `len(p)` across `s`, maintaining a `s_count` dictionary.
- At each step, update the window by:
  - Removing the character going out
  - Adding the character coming in
- Compare `s_count` with `p_count`. If they match, it's an anagram, and the start index is added to the result.

This avoids sorting or rebuilding the frequency map from scratch, and is efficient for long strings.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`  
  Each character is processed once when added and once when removed from the window.

- **Space Complexity:** `O(1)`  
  The space is bounded by the number of lowercase letters (at most 26).
