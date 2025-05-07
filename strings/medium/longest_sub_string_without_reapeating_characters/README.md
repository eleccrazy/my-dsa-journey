# Longest Substring Without Repeating Characters

## Problem Statement

Given a string `s`, return the length of the **longest substring** that contains **no repeating characters**.

A substring is a contiguous sequence of characters within the string.  
Characters in the substring must all be unique.

---

## Examples

### Example 1
```python
s = "abcabcbb"
output = 3
```
**Explanation:**
The longest substring without repeating characters is `"abc"`, which has a length of 3.

### Example 2
```python
s = "bbbbb"
output = 1
```
**Explanation:**
The longest substring without repeating characters is `"b"`, which has a length of 1.

### Example 3
```python
s = "pwwkew"
output = 3
```
**Explanation:**
The longest substring without repeating characters is `"wke"`, which has a length of 3.
The substring `"pwke"` is not valid because the characters are not contiguous.

---

## Constraints

- `0 <= s.length <= 5 * 10⁴`
- `s` consists of English letters, digits, symbols, and spaces

---

## Solution Overview

This solution uses a **variable-size sliding window** and a **set** to track the characters in the current substring window.

- Initialize two pointers `left` and `right` at the start of the string.
- Expand the window by moving `right` forward if the character is not in the set.
- If a duplicate is found, shrink the window by moving `left` and removing the left character from the set.
- At each step, update the maximum length of a valid (duplicate-free) window.

This ensures that the substring in the window always contains unique characters.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`  
  Each character is added and removed from the set at most once.

- **Space Complexity:** `O(k)`  
  Where `k` is the number of unique characters in the current window (at most all printable ASCII characters).
