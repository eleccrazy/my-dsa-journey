# Climbing Stairs

## Problem Statement

You are climbing a staircase. It takes `n` steps to reach the top.  
Each time you can either climb **1 or 2 steps**.  
In how many **distinct ways** can you climb to the top?

---

## Examples

### Example 1  
Input: `n = 2`  
Output: `2`  
Explanation:  
1. 1 step + 1 step  
2. 2 steps

### Example 2  
Input: `n = 3`  
Output: `3`  
Explanation:  
1. 1 step + 1 step + 1 step  
2. 1 step + 2 steps  
3. 2 steps + 1 step

---

## Constraints

- `1 <= n <= 45`

## Solution Overview

Solve Climbing Stairs using top-down recursion with memoization

- The number of ways to reach step n is the sum of ways to reach (n-1) and (n-2)
- Base cases: 1 way to climb 1 step, 2 ways to climb 2 steps
- Use a memoization dictionary to avoid recomputing overlapping subproblems

## Complexity Analysis

- **Time Complexity:** `O(n)`  
  Each value from 1 to n is computed only once.

- **Space Complexity:** `O(n)`  
  Due to the memoization table and recursive call stack.


