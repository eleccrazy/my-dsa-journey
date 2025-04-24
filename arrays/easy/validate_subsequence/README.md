# Validate Subsequence

## Problem Statement

Given two non-empty arrays of integers, write a function that determines whether the second array is a **subsequence** of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but **must be in the same order** as they appear in the array.

---

## Examples

### Example 1
- Input: array = [1, 2, 3, 4, 5], sequence = [1, 3, 4]
- Output: True

### Example 2
- array = [5, 1, 22, 25, 6, -1, 8, 10], sequence = [1, 6, -1, 10]
- Output: True

### Example 3
- array = [1, 2, 3, 4], sequence = [2, 1]
- Output: False


---

## Notes

- The numbers in the sequence must appear in order but **do not** need to be adjacent.
- The function should return a boolean: `True` if the sequence is valid, `False` otherwise.
- You can assume the arrays contain only integers and are non-empty.
