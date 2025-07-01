# Valid Parentheses

## Problem Statement

Given a string `s` containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is **valid**.

A string is considered **valid** if:

- Every open bracket has a corresponding **closing bracket** of the **same type**.
- Open brackets are closed **in the correct order**.
- Every closing bracket must match the most recent unmatched opening bracket.
---

## Examples

### Example 1
Input: `s = "()"`
Output: `true`
### Example 2
Input: `s = "()[]{}"`
Output: `true`
### Example 3
Input: `s = "(]"`
Output: `false`
### Example 4
Input: `s = "([])"`
Output: `true`
### Example 5
Input: `s = "([)]"`
Output: `false`


---

## Constraints

- `1 <= s.length <= 10⁴`
- `s` consists only of the characters `'()[]{}'`

## Solution Overview

This solution uses a **stack** to match parentheses using a bracket map (`{ '(': ')', '{': '}', '[': ']' }`).

## Complexity Analysis

- **Time Complexity:** `O(n)`  
  Each character is processed once.

- **Space Complexity:** `O(n)`  
  In the worst case (all open brackets), the stack size grows to `n`.