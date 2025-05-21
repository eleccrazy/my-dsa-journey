"""
File: space_optimized_solution.py
Description: This module contains a space-optimized solution to the Intersection of Two Linked Lists problem.
Author: Gizachew Kassa
Date: 21-05-2025
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    """
    Uses two pointers that traverse both lists. When a pointer reaches the end of one list,
    it jumps to the head of the other. If the lists intersect, the pointers will eventually
    meet at the intersection node; otherwise, both will reach the end (None) simultaneously.

    Time Complexity: O(n + m)
    Space Complexity: O(1)
    """
    pointerA = headA
    pointerB = headB

    while pointerA != pointerB:
        pointerA = pointerA.next if pointerA else headB
        pointerB = pointerB.next if pointerB else headA

    return pointerA
