# String to Integer (atoi)

## Problem Statement

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer according to the following rules:

1. **Whitespace**: Ignore any leading whitespace characters.
2. **Signedness**: Check for an optional `'+'` or `'-'` sign character to determine the sign of the number.
3. **Conversion**: Read in the digits until a non-digit character or end of string is reached.
4. **No Digits Case**: If no digits are found, return `0`.
5. **Clamping**: Clamp the result within the 32-bit signed integer range:  
   - Minimum: `-2³¹`  
   - Maximum: `2³¹ - 1`

Return the final integer result.

---

## Examples

### Example 1

```python
s = "42"
result = myAtoi(s)
# Output: 42
```

### Example 2

```python
s = "   -42"
result = myAtoi(s)
# Output: -42
```
### Example 3

```python
s = "4193 with words"
result = myAtoi(s)
# Output: 4193
```

## Constraints
 - 0 <= s.length <= 200

 - s consists of English letters (uppercase and lowercase), digits (0-9), whitespace (' '), '+', '-', and '.'

---

## Solution Overview

This solution mimics the behavior of the C `atoi` function by following a step-by-step parsing approach:

- **Trim Leading Whitespace**: Use `lstrip()` to ignore any leading whitespace characters.
- **Handle Optional Sign**: Check if the first non-space character is `'+'` or `'-'` and determine the sign accordingly.
- **Parse Digits**: Iterate through the remaining characters, reading digits until a non-digit character is encountered.
- **Convert to Integer**: Convert the accumulated digit string to an integer. If no digits were found, return `0`.
- **Clamp to 32-bit Signed Range**: Ensure the result is within the range `[-2³¹, 2³¹ - 1]`. Clamp the value if it exceeds the limits.

This approach explicitly follows the problem's parsing rules and handles common edge cases like empty input, invalid characters, and overflows.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`  
  Where `n` is the length of the input string. We scan the string at most once.

- **Space Complexity:** `O(n)`  
  Due to building the intermediate `formed_number` string.
