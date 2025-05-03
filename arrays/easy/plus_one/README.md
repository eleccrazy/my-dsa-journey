# Plus One
## Problem Statement
You are given a large integer represented as an array of digits, where each digit is stored in a separate element of the array. The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
The integer does not contain any leading zeros, except for the number 0 itself.
You need to add one to the integer represented by the array and return the resulting array of digits. The result should also be represented in the same format, with each digit stored in a separate element of the array.

## Examples
### Example 1
- Input: digits = [1, 2, 3]
- Output: [1, 2, 4]
- Explanation: The integer represented by the array is 123. Adding one gives 124, which is represented as [1, 2, 4].

### Example 2
- Input: digits = [4, 3, 2, 1]
- Output: [4, 3, 2, 2]
- Explanation: The integer represented by the array is 4321. Adding one gives 4322, which is represented as [4, 3, 2, 2].

### Example 3
- Input: digits = [9]
- Output: [1, 0]
- Explanation: The integer represented by the array is 9. Adding one gives 10, which is represented as [1, 0].

## Constraints
- 1 <= digits.length <= 100
- 0 <= digits[i] <= 9
- digits does not contain any leading zeros, except for the number 0 itself.
- The input array represents a non-negative integer.

## Solution Overview
The solution iterates through the array of digits from the last element to the first. It adds one to the last digit and checks if it results in a carry (i.e., if the digit becomes 10). If there is a carry, it sets the current digit to 0 and moves to the next digit. If there is no carry, it simply returns the modified array.

## Complexity Analysis
- **Time Complexity:** O(n)  
  The algorithm iterates through the array once, where n is the length of the array.
- **Space Complexity:** O(1)
    The algorithm modifies the input array in place and does not use any additional space proportional to the input size.