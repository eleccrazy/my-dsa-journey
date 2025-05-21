# Design Linked List

## Problem Statement

Design your implementation of a linked list. You can choose to use a **singly** or **doubly** linked list.

Each node in a singly linked list should have two attributes:
- `val`: the value of the node
- `next`: a reference to the next node

If using a doubly linked list, nodes should also have:
- `prev`: a reference to the previous node

Assume all nodes are 0-indexed.

Implement the `MyLinkedList` class with the following methods:

### Methods

- `MyLinkedList()`  
  Initializes the linked list.

- `int get(int index)`  
  Returns the value of the `index`th node in the linked list. If the index is invalid, return `-1`.

- `void addAtHead(int val)`  
  Adds a node of value `val` before the first element of the linked list. The new node becomes the head.

- `void addAtTail(int val)`  
  Appends a node of value `val` at the end of the linked list.

- `void addAtIndex(int index, int val)`  
  Adds a node of value `val` **before** the `index`th node in the linked list.  
  If `index == length` of the list, the node is appended at the end.  
  If `index > length`, the node is not inserted.

- `void deleteAtIndex(int index)`  
  Deletes the node at the `index`th position, if the index is valid.

---

## Example

### Example 1
```python
Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [0], [0]]
Output
[null, null, null, null, 2, null, 1]
```

---

## Constraints

- `0 <= index, val <= 1000`
- At most `2000` calls will be made to `get`, `addAtHead`, `addAtTail`, `addAtIndex`, and `deleteAtIndex`.
- You **may not use built-in linked list libraries**.

