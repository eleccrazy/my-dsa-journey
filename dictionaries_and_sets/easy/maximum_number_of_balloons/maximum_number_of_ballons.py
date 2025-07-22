"""
File: maximum_number_of_balloons.py
Description: This module calculates the maximum number of times the word "balloon" can be formed from a given string using character frequency counting.
Author: Gizachew Kassa
Date: 22-07-2025
"""


def maxNumberOfBalloons(text: str) -> int:
    """
    Calculates the maximum number of 'balloon' instances that can be formed
    from the given input text by counting character frequencies.

    Time Complexity: O(n)
    - Each character in the text is processed once.

    Space Complexity: O(1)
    - Only a fixed-size dictionary is used for five letters.

    """
    required_letters = {"b", "a", "l", "o", "n"}
    freq = {ch: 0 for ch in required_letters}

    for ch in text:
        if ch in freq:
            freq[ch] += 1

    # l and o are needed twice for each balloon
    freq["l"] //= 2
    freq["o"] //= 2

    return min(freq.values())
