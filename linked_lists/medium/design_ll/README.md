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

## Solution Overview

This implementation uses a **singly linked list** data structure with basic node manipulation operations. Each node contains:
- `value`: the integer value of the node
- `next`: a reference to the next node in the list

The `MyLinkedList` class supports the following operations:

- **get(index)**: Traverses from the head to the given index and returns the node's value if valid, otherwise returns `-1`.
- **addAtHead(val)**: Inserts a new node at the beginning of the list and updates the head.
- **addAtTail(val)**: Traverses to the end of the list and appends the new node.
- **addAtIndex(index, val)**: Traverses to the node just before the given index and inserts the new node. Handles edge cases like insertion at head, tail, and invalid index.
- **deleteAtIndex(index)**: Removes the node at the specified index by adjusting the previous node's `next` pointer. Handles head deletion and invalid indices.

An internal `size` counter is maintained to validate indices in constant time.

---

## Complexity Analysis

- **Time Complexity:**
  - `get(index)`: O(n)
  - `addAtHead(val)`: O(1)
  - `addAtTail(val)`: O(n)
  - `addAtIndex(index, val)`: O(n)
  - `deleteAtIndex(index)`: O(n)

  > Most operations involve traversing the list to find the correct node, resulting in linear time in the worst case.

- **Space Complexity:** O(n)
    - The space complexity is O(n) due to the storage of nodes in the linked list.
    - The implementation uses a constant amount of extra space for pointers and counters.