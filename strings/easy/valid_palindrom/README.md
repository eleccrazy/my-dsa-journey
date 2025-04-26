# Valid Palindrome

## Problem Statement

A phrase is a palindrome if, after:
- Converting all uppercase letters into lowercase letters
- Removing all non-alphanumeric characters

it reads the same forward and backward.

Alphanumeric characters include letters and numbers only.

Given a string `s`, return `True` if it is a palindrome, or `False` otherwise.

---

## Examples

### Example 1
- Input: s = "A man, a plan, a canal: Panama"
- Output: true
- Explanation: "amanaplanacanalpanama" is a palindrome.

### Example 2
- Input: s = "race a car"
- Output: false
- Explanation: "raceacar" is not a palindrome.

### Example 3
- Input: s = " "
- Output: true
- Explanation: s is an empty string "" after removing non-alphanumeric characters. Since an empty string reads the same forward and backward, it is a palindrome.


---

## Constraints

- 1 <= s.length <= 2 × 10⁵
- `s` consists only of printable ASCII characters.

---

## Solution Overview

This solution first preprocesses the input string by:
- Converting all letters to lowercase
- Removing all non-alphanumeric characters

After cleaning, a two-pointer technique is used to check whether the string reads the same forward and backward.

---

### Complexity Analysis

- **Time Complexity:** O(n)  
  One pass to clean the string and one pass to check for palindrome.
  
- **Space Complexity:** O(n)  
  Additional space is used to store the cleaned version of the input string.
