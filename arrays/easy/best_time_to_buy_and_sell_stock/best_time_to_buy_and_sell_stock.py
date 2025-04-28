"""
File: best_time_to_buy_and_sell_stock.py
Description: finds the maximum profit from buying and selling stock once
Author: Gizachew Kassa
Date: 29/04/2025
"""

from typing import List


def maxProfit(self, prices: List[int]) -> int:
    """
    Calculates the maximum profit by buying and selling stock once.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(prices) < 2:
        return 0

    minimum = prices[0]
    profit = float("-inf")

    for i in range(1, len(prices)):
        if prices[i] < minimum:
            minimum = prices[i]
        dif = prices[i] - minimum
        profit = max(dif, profit)

    return profit
