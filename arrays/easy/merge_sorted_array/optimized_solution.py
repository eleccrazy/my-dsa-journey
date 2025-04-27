""" """

from typing import List


def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Merges two sorted arrays in-place using a two-pointer approach.

    Starts from the end of both arrays, placing the larger element
    at the correct position in nums1.

    Time Complexity: O(m + n)
    Space Complexity: O(1)

    """
    ptr1 = m - 1  # last valid element of nums1
    ptr2 = n - 1  # last element of nums2
    p = m + n - 1  # last postion after merging both (currently at nums1)

    while ptr2 >= 0:
        if ptr1 >= 0 and nums1[ptr1] > nums2[ptr2]:
            nums1[p] = nums1[ptr1]
            ptr1 -= 1
        else:
            nums1[p] = nums2[ptr2]
            ptr2 -= 1
        p -= 1

    # Copy remaining elements from nums2 to nums1
    while ptr2 >= 0:
        nums1[p] = nums2[ptr2]
        ptr2 -= 1
        p -= 1

    # Copy remaining elements from nums2 to nums1
    while ptr2 >= 0:
        nums1[p] = nums2[ptr2]
        ptr2 -= 1
        p -= 1
