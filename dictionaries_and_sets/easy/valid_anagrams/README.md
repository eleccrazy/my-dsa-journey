# Valid Anagram

## Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

---

## Examples

### Example 1  
Input: `s = "anagram"`, `t = "nagaram"`  
Output: `true`

### Example 2  
Input: `s = "rat"`, `t = "car"`  
Output: `false`

---

## Constraints

- `1 <= s.length, t.length <= 5 * 10⁴`
- `s` and `t` consist of **lowercase English letters** only

## Solution Overview

Solve Valid Anagram using hash map frequency counting

- Return False immediately if lengths differ
- Count the frequency of each character in `t`
- Subtract frequencies while scanning `s`, ensuring all characters match
- If any count goes negative or is missing, the strings are not anagrams

## Complexity Analysis

- **Time Complexity:** `O(n)`  
  Each character in both strings is visited once.

- **Space Complexity:** `O(1)`  
  Hash map stores frequencies of lowercase letters (at most 26 keys).
