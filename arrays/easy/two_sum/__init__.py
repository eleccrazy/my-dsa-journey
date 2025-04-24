"""
Two Number Sum - Multiple Approaches

This package contains different implementations of the Two Number Sum problem:
1. Brute Force
2. Hash Table (Optimal)
3. Two Pointers (after sorting)

Usage:
    from two_sum import (
        two_number_sum_bruteforce,
        two_number_sum_hash_table,
        two_number_sum_two_pointers
    )
"""

from .brute_force import two_number_sum_bruteforce
from .hash_table import two_number_sum_hash_table
from .two_pointers import two_number_sum_two_pointers

__all__ = [
    "two_number_sum_bruteforce",
    "two_number_sum_hash_table",
    "two_number_sum_two_pointers",
]
