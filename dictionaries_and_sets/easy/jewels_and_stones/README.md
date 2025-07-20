# Jewels and Stones

## Problem Statement

You're given strings `jewels` representing the types of stones that are jewels,  
and `stones` representing the stones you have. Each character in `stones` is a type of stone you possess.  
You want to know how many of the stones you have are also jewels.

Letters are **case sensitive**, so `"a"` is considered a different type of stone from `"A"`.

---

## Examples

### Example 1  
Input: `jewels = "aA"`, `stones = "aAAbbbb"`  
Output: `3`

### Example 2  
Input: `jewels = "z"`, `stones = "ZZ"`  
Output: `0`

---

## Constraints

- `1 <= jewels.length, stones.length <= 50`
- `jewels` and `stones` consist of only English letters
- All the characters in `jewels` are **unique**

---

## Solution Overview

Solve Jewels and Stones using a set for fast lookup

- Convert `jewels` string to a set for O(1) membership testing
- Iterate through `stones` and count characters that appear in the jewels set
- Case-sensitive comparison ensures distinct jewel types

---

## Complexity Analysis

- **Time Complexity:** `O(n + m)`  
  Where `n` is the length of `stones`, and `m` is the length of `jewels`.  
  Set construction takes `O(m)` and traversal of `stones` takes `O(n)`.

- **Space Complexity:** `O(m)`  
  Additional space used to store the jewel types in a set.
