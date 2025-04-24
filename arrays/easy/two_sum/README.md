# Two Number Sum

## Problem Statement

Write a function that takes in:

- A **non-empty array** of **distinct integers**
- An integer **target sum**

Return an array containing **any two numbers** from the input array that **sum to the target sum**.  
If no such pair exists, return an empty array.

- The two numbers must be **different** (no using the same number twice).
- You can return the pair in **any order**.
- You can assume there is **at most one valid pair**.

---

## Examples

### Example 1
- Input: array = [3, 5, -4, 8, 11, 1, -1, 6], targetSum = 10
- Output: [-1, 11]

### Example 2
- Input: array = [4, 6], targetSum = 10
- Output: [4, 6]

### Example 3
- Input: array = [1, 2, 3, 4, 5], targetSum = 10
- Output: []


---

## Constraints

- Input array length ≥ 2
- All integers in the array are **distinct**
- Only one valid pair exists (or none)

---

## Solution Approaches

### 1. Brute Force (Nested Loops)

- Loop through every pair of elements
- Check if they sum up to the target

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

---

### 2. Hash Table (Optimal – One-Pass)

- Iterate through the array while storing the **complement** (`y = target - num`) in a set
- If you find the complement, return the pair

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

---

### 3. Two Pointers (After Sorting)

- Sort the array
- Use two pointers (`left`, `right`) to find a pair that sums to the target

**Time Complexity:** O(n log n) for sorting + O(n) for the two-pointer search = O(n log n)
**Space Complexity:** O(1)

---

> Check this folder for code in all 3 styles:  
> `brute_force.py`, `hash_table.py`, `two_pointers.py`
