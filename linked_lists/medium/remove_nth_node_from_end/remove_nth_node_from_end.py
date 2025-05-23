"""
File: remove_nth_node_from_end.py
Description: This module contains a function to remove the nth node from the end of a linked list.
Author: Gizachew Kassa
Date: 23-05-2025
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Removes the nth node from the end of the linked list using a one-pass two-pointer technique.

    A dummy node is used to simplify edge cases like deleting the head. The right pointer
    is advanced n+1 steps ahead of the left pointer to maintain a gap. Both pointers are then
    moved together until the right pointer reaches the end. The node after the left pointer is removed.

    Time Complexity: O(n) - Single pass through the list
    Space Complexity: O(1) - Constant space used
    """
    dummy = ListNode(0, head)
    left_ptr = dummy
    right_ptr = dummy

    for _ in range(n + 1):
        right_ptr = right_ptr.next

    while right_ptr:
        left_ptr = left_ptr.next
        right_ptr = right_ptr.next

    left_ptr.next = left_ptr.next.next

    return dummy.next
