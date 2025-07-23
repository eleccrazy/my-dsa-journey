"""
File: group_anagrams.py
Description: This module groups a list of strings into anagrams using character frequency counting.
Author: Gizachew Kassa
Date: 23-07-2025
"""

from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    Groups anagrams from a list of strings using character frequency as a key.

    Time Complexity: O(n * k)
    - n is the number of strings
    - k is the maximum string length
    - Each string is processed in O(k) time to compute its character frequency

    Space Complexity: O(n * k)
    - Stores all original strings and their groupings
    - Frequency keys are tuples of size 26 (constant space per key)

    """
    anagrams_dict = defaultdict(list)

    for s in strs:
        # Create a frequency count for each character a-z
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1

        # Use the frequency count as a hashable key
        key = tuple(count)
        anagrams_dict[key].append(s)

    return list(anagrams_dict.values())
