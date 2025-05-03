# Roman to Integer
## Problem
Given a string `s` representing a roman numeral, convert it to an integer.
Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.
- `I` is 1.
- `V` is 5.
- `X` is 10.
- `L` is 50.
- `C` is 100.
- `D` is 500.
- `M` is 1000.
For example, `II` is 2, `XIII` is 13, and `XXI` is 21.
Roman numerals are usually written largest to smallest from left to right.

However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C (100) to make 40 and 90.
- C can be placed before D (500) and M (1000) to make 400 and 900.

## Examples
### Example 1
- Input: s = "III"
- Output: 3
- Explanation: III = 3.

### Example 2
- Input: s = "IV"
- Output: 4
- Explanation: IV = 4.

### Example 3
- Input: s = "IX"
- Output: 9
- Explanation: IX = 9.

### Example 4
- Input: s = "LVIII"
- Output: 58
- Explanation: L = 50, V= 5, III = 3.
- Explanation: LVIII = 50 + 5 + 3 = 58.

## Constraints
- 1 <= s.length <= 15
- `s` contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that `s` is a valid roman numeral in the range [1, 3999].

## Solution Overview
The solution uses a dictionary to map each roman numeral to its corresponding integer value. It then iterates through the string, checking if the current numeral is less than the next numeral. If it is, it subtracts the current numeral's value from the total; otherwise, it adds it. This approach efficiently handles both addition and subtraction cases in a single pass.

## Complexity Analysis
- **Time Complexity:** O(n)  
  The algorithm iterates through the string once, where n is the length of the string.
- **Space Complexity:** O(1)
    - The space complexity is O(1) because the size of the dictionary is constant and does not depend on the input size.
    - The algorithm uses a fixed amount of space for variables and the dictionary, regardless of the input size.

