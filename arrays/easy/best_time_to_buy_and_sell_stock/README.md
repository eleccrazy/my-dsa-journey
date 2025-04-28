# Best Time to Buy and Sell Stock

## Problem Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`-th day.

You want to maximize your profit by choosing:

- A single day to **buy** one stock
- A different day in the future to **sell** that stock

Return the maximum profit you can achieve from this transaction.  
If no profit can be achieved, return `0`.

---

## Examples

### Example 1

```python
prices = [7, 1, 5, 3, 6, 4]
```
**Output:** `5`
**Explanation:** Buy on day `2` (price = `1`) and sell on day `5` (price = `6`), profit = `6 - 1 = 5`.
**Note:** Buying on day `2` and selling on day `1` is not allowed because you must buy before you sell.

### Example 2

```python
prices = [7, 6, 4, 3, 1]
```
**Output:** `0`
**Explanation:** In this case, no transactions are done and the max profit = `0`.
**Note:** You cannot buy and sell on the same day.

## Constraints

- 1 <= prices.length <= 10⁵
- 0 <= prices[i] <= 10⁴

## Solution Overview

This solution uses a **One-Pass Two-Variable Approach**:

- Maintain the minimum price seen so far while iterating.
- For each day, calculate the profit if selling on that day (`current price - minimum so far`).
- Update the maximum profit found so far during the traversal.
- Return the maximum profit at the end.

---

### Complexity Analysis

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
