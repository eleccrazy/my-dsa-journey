# Maximum Number of Balloons

## Problem Statement

Given a string `text`, you want to use the characters of `text` to form as many instances of the word `"balloon"` as possible.

You can use each character in `text` **at most once**.  
Return the **maximum number** of instances that can be formed.

---

## Examples

### Example 1  
Input: `text = "nlaebolko"`  
Output: `1`

### Example 2  
Input: `text = "loonbalxballpoon"`  
Output: `2`

### Example 3  
Input: `text = "leetcode"`  
Output: `0`

---

## Constraints

- `1 <= text.length <= 10⁴`
- `text` consists of **lowercase English letters** only

## Solution Overview

Solve Maximum Number of Balloons by counting required letters

- Create a frequency map for the characters `'b'`, `'a'`, `'l'`, `'o'`, and `'n'`
- Iterate over the input string and count how many of each required letter appears
- Divide the count of `'l'` and `'o'` by 2 since they are needed twice
- Return the minimum value among all letter counts to get the number of "balloon" instances

## Complexity Analysis

- **Time Complexity:** `O(n)`  
  Each character in `text` is processed once.

- **Space Complexity:** `O(1)`  
  Only a fixed-size dictionary for 5 letters is used, regardless of input size.
