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
