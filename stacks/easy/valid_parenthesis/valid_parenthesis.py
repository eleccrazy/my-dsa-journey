"""
File: valid_parenthesis.py
Description: This module contains a function to check if a string of parentheses is valid.
Author: Gizachew Kassa
Date: 30-06-2025
"""


def isValid(self, s: str) -> bool:
    """
    Validates whether the input string has properly matched and ordered brackets.

    Uses a stack to process each character:
    - Pushes any character onto the stack.
    - Pops if the current character matches the expected closing bracket
      for the last opening bracket in the stack.

    This approach assumes all characters are one of '(){}[]' per problem constraints.

    Time Complexity: O(n)
    - Each character is pushed and popped at most once.

    Space Complexity: O(n)
    - Stack can grow up to the size of the input string in the worst case.

    Returns:
        bool: True if the string is valid, False otherwise.
    """
    brack_map = {"(": ")", "{": "}", "[": "]"}
    stack = []

    if len(s) < 2 or s[0] not in brack_map:
        return False

    stack.append(s[0])

    for c in s[1:]:
        if stack and c == brack_map.get(stack[-1]):
            stack.pop()
        else:
            stack.append(c)

    return len(stack) == 0
