# Reverse Words in a String

## Problem Statement

Given an input string `s`, reverse the **order of the words**.

A word is defined as a sequence of non-space characters. The words in `s` will be separated by **at least one space**.

Return a string of the words in reverse order, **concatenated by a single space**.

Note:
- `s` may contain **leading or trailing spaces**, or **multiple spaces between words**.
- The returned string should have **only one space** separating the words and **no extra spaces** at the start or end.

---

## Examples

### Example 1

```python
s = "the sky is blue"
Output: "blue is sky the"
```

### Example 2

```python
s = "  hello world  "
Output: "world hello"
```
### Example 3

```python
s = "a good   example"
Output: "example good a"
```

---

## Constraints

- `1 <= s.length <= 10⁴`
- `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.
- There is at least one word in `s`.

---

## Solution Overview

This solution uses a **split–reverse–join** strategy:

- Use `split()` to divide the string into a list of words. This automatically removes leading, trailing, and multiple intermediate spaces.
- Reverse the list in place using slicing (`[::-1]`).
- Join the reversed list into a string using `' '.join()` to ensure exactly one space between words.

This approach efficiently handles all whitespace issues while reversing word order.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`  
  The entire string is processed linearly through splitting, reversing, and joining.

- **Space Complexity:** `O(n)`  
  Extra space is used to store the list of words.
