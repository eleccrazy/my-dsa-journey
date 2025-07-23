# Group Anagrams

## Problem Statement

Given an array of strings `strs`, group the anagrams together.  
You can return the answer in **any order**.

---

## Examples

### Example 1  
Input: `strs = ["eat","tea","tan","ate","nat","bat"]`  
Output: `[["bat"],["nat","tan"],["ate","eat","tea"]]`

### Example 2  
Input: `strs = [""]`  
Output: `[[""]]`

### Example 3  
Input: `strs = ["a"]`  
Output: `[["a"]]`

---

## Constraints

- `1 <= strs.length <= 10⁴`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of **lowercase English letters**

## Solution Overview

Solve Group Anagrams by using a character frequency signature

- For each word, count how many times each letter (a–z) appears
- Use the frequency count (as a tuple) as a key in a hash map
- Group all words with the same signature together
- Return the grouped values from the hash map

## Complexity Analysis

- **Time Complexity:** `O(n * k)`  
  Where `n` is the number of words and `k` is the maximum length of a word.  
  Each word requires O(k) time to build its frequency count.

- **Space Complexity:** `O(n * k)`  
  Storing all words and their groupings, and the frequency map keys.
