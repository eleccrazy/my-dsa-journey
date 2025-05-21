# Intersection of Two Linked Lists

## Problem Statement

Given the heads of two singly linked-lists `headA` and `headB`, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return `null`.

Note that the linked lists must **retain their original structure** after the function returns.

The test cases are generated such that there are **no cycles** anywhere in the entire linked structure.

### Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

- `intersectVal` - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
- `listA` - The first linked list.
- `listB` - The second linked list.
- `skipA` - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
- `skipB` - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.

The judge will create the linked structure based on these inputs and pass the two heads, `headA` and `headB`, to your program.

If you correctly return the intersected node, then your solution will be accepted.

---

## Examples

### Example 1
```python
Input: headA = [4,1,8,4,5], headB = [5,0,1,8,4,5], intersectVal = 8, skipA = 2, skipB = 3
Output: Intersected at '8'
```
### Example 2
```python
Input: headA = [1,9,1,2,4], headB = [3,2,4], intersectVal = 2, skipA = 3, skipB = 1
Output: Intersected at '2'
```
### Example 3
```python
Input: headA = [2,6,4], headB = [1,5], intersectVal = 0, skipA = 3, skipB = 2
Output: No intersection
```

---

## Constraints

- The number of nodes of `listA` is in the range `[0, 10⁴]`.
- The number of nodes of `listB` is in the range `[0, 10⁴]`.
- `1 <= Node.val <= 10⁵`
- `0 <= skipA < listA.length`
- `0 <= skipB < listB.length`
- `intersectVal` is 0 if `listA` and `listB` do not intersect.
- `intersectVal == listA[skipA] == listB[skipB]` if `listA` and `listB` intersect.

---

## Follow-up

Could you write a solution that runs in `O(n)` time and uses only `O(1)` memory?

