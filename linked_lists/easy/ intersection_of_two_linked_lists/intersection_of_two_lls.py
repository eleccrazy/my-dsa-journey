"""
File: intersection_of_two_lls.py
Description: This module contains a solution to the Intersection of Two Linked Lists problem.
Author: Gizachew Kassa
Date: 21-05-2025
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    """
    Finds the intersection node of two singly linked lists using a hash set.

    Args:
        headA (ListNode): The head of the first linked list.
        headB (ListNode): The head of the second linked list.

    Returns:
        ListNode or None: The node at which the two lists intersect, or None if they do not intersect.

    Time Complexity: O(n + m)
        - n is the number of nodes in list A
        - m is the number of nodes in list B

    Space Complexity: O(n)
        - Uses a set to store references to nodes in list A
    """
    a_nodes = set()

    while headA:
        a_nodes.add(headA)
        headA = headA.next

    while headB:
        if headB in a_nodes:
            return headB
        headB = headB.next

    return None
