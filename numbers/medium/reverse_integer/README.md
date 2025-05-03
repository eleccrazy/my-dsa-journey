# Reverse Integer

## Problem Statement

Given a signed 32-bit integer `x`, return `x` with its digits reversed.  
If reversing `x` causes it to go outside the signed 32-bit integer range `[-2³¹, 2³¹ - 1]`, return `0`.

You must **not use 64-bit integers**, even temporarily.

---

## Examples

### Example 1

```python
x = 123
Output: 321
```
### Example 2

```python
x = -123
Output: -321
```
### Example 3

```python
x = 120
Output: 21
```

## Constraints
---

## Constraints

- `-2³¹ <= x <= 2³¹ - 1`

---

## Solution Overview

This solution uses **string manipulation** to reverse the digits of the given integer:

- First, check if the number is negative and make it positive for easier processing.
- Convert the number to a string and reverse it using slicing (`[::-1]`).
- Convert the reversed string back to an integer and re-apply the negative sign if needed.
- Check if the reversed number lies within the 32-bit signed integer range.
- If it overflows, return `0`; otherwise, return the reversed integer.

This method is fast to implement and easy to reason about, especially for interview scenarios.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`  
  Where `n` is the number of digits in the input integer. String conversion and reversal are linear in the number of digits.

- **Space Complexity:** `O(n)`  
  Temporary space is used to store the string representation and the reversed string.
