# Merge Strings Alternately

## Problem Statement

You are given two strings `word1` and `word2`.  
Merge the strings by adding letters in **alternating order**, starting with `word1`.  
If one string is longer than the other, append the remaining letters at the end of the merged string.

Return the merged string.

---

## Examples

### Example 1
Input: `word1 = "abc", word2 = "pqr"`
Output: `"apbqcr"`
### Example 2
Input: `word1 = "ab", word2 = "pqrs"`
Output: `"apbqrs"`
### Example 3
Input: `word1 = "abcd", word2 = "pq"`
Output: `"apbqcd"`



---

## Constraints

- `1 <= word1.length, word2.length <= 100`
- `word1` and `word2` consist of **lowercase English letters only**

## Solution Overview

The solution merges two input strings character by character in alternating order.

- Iterate through both strings up to the length of the shorter one.
- At each step, append one character from each string.
- After the loop, if one string is longer, append the remaining characters from it to the result.

This approach handles both equal and unequal length inputs efficiently and ensures correct merge order.

## Complexity Analysis

- **Time Complexity:** `O(n)`
  - Linear with respect to the total number of characters in both strings.
- **Space Complexity:** `O(n)`
  - Result string stores the merged characters.

