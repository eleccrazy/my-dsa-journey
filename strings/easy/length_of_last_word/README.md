# Length of Last Word
## Problem
Given a string `s` consisting of words and spaces, return the length of the last word in the string.
A word is defined as a maximal substring consisting of non-space characters only.
The input string `s` can contain leading and trailing spaces, and there may be multiple spaces between words.

## Examples
### Example 1
- Input: s = "Hello World"
- Output: 5
- Explanation: The last word is "World", which has a length of 5.

### Example 2
- Input: s = "   fly me   to   the moon  "
- Output: 4
- Explanation: The last word is "moon", which has a length of 4.

## Constraints
- 1 <= s.length <= 10^4
- `s` consists of only English letters and spaces.
- There will be at least one word in `s`.
- The input string `s` can contain leading and trailing spaces, and there may be multiple spaces between words.

## Solution Overview
The solution uses the `split()` method to break the string into words based on spaces. It then retrieves the last word from the list of words and returns its length. This approach efficiently handles leading and trailing spaces, as well as multiple spaces between words.

## Complexity Analysis
- **Time Complexity:** O(n)  
  The algorithm iterates through the string once to split it into words, where n is the length of the string.
- **Space Complexity:** O(n)
    The space complexity is O(n) because the split operation creates a list of words, which can be proportional to the length of the input string in the worst case.
