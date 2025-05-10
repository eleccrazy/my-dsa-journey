# Longest Repeating Character Replacement

## Problem Statement

You are given a string `s` consisting of **only uppercase English letters**, and an integer `k`.

You can **replace at most `k` characters** in the string with any other uppercase letter.  
Return the **length of the longest substring** that can be obtained where **all characters are the same**, after at most `k` replacements.

---

## Examples

### Example 1

**Input:**
```python
s = "AABABBA"
k = 1
```
**Output:**
```python
4
```
**Explanation:**  
Replace the 'A' at index 4 with 'B' to get `"AABBBBA"` → substring `"BBBB"` is length 4.  
Other valid strategies may exist too.

### Example 2
**Input:**
```python
s = "AA"
k = 2
```
**Output:**
```python
2
```
**Explanation:**
The entire string can be replaced, so the length is 2.

---

## Constraints

- `1 <= s.length <= 10⁵`
- `s` consists of only **uppercase English letters (A–Z)`
- `0 <= k <= s.length`

---

## Solution Overview

This solution uses a **variable-size sliding window** strategy:

- It maintains a window `[left, right]` and tracks the frequency of characters within that window.
- The idea is to find the longest window where at most `k` characters can be replaced to make the entire window consist of the same character.
- The most frequent character in the window (`max_freq`) determines how many characters need to be replaced:  
  `window_size - max_freq <= k`
- If the window becomes invalid, it is shrunk from the left.
- The maximum valid window length is tracked and returned.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`  
  Each character is processed at most twice — once when added and once when removed from the window.

- **Space Complexity:** `O(1)`  
  The character frequency map stores at most 26 keys (uppercase English letters).
