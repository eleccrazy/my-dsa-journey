"""
File: merge_intervals.py
Description: This module contains a function to merge overlapping intervals in a list of intervals.
Author: Gizachew Kassa
Date: 14-06-2025
"""

from typing import List


def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    """
    Merges all overlapping intervals in a list of intervals.

    Time Complexity: O(n log n)
    - Due to sorting the list of intervals.

    Space Complexity: O(n)
    - To store the merged result.
    """
    result = []

    # Sort the intervals by starting time
    intervals.sort(key=lambda x: x[0])

    if len(intervals) < 2:
        return intervals

    curr_start, curr_end = intervals[0]

    for interval in intervals[1:]:
        if curr_end >= interval[0]:
            # Overlapping interval, merge by extending the end
            curr_end = max(curr_end, interval[1])
        else:
            # Non-overlapping interval, add current and reset
            result.append([curr_start, curr_end])
            curr_start, curr_end = interval

    # Append the last interval
    result.append([curr_start, curr_end])

    return result
