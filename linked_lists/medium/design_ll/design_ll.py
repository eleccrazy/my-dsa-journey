"""
File: design_ll.py
Description: This module contains a class that implements a basic design of a linked list.
Author: Gizachew Kassa
Date: 21-05-2025
"""


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class MyLinkedList:
    """
    Implements a singly linked list with support for basic operations such as:
    get, add at head, add at tail, add at index, and delete at index.

    Time Complexity:
    - get, addAtIndex, deleteAtIndex: O(n)
    - addAtHead, addAtTail: O(n) in worst case (tail is not cached)

    Space Complexity: O(n) for n nodes stored
    """

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.value

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return

        new_node = Node(val)
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1
