# Product of Array Except Self

## Problem Statement

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the **product of all the elements** of `nums` **except** `nums[i]`.

The solution must:
- Run in `O(n)` time
- **Not use division**
- Ensure the product fits within a 32-bit integer

---

## Examples

### Example 1
Input: `nums = [1, 2, 3, 4]`
Output: `[24, 12, 8, 6]`
### Example 2
Input: `nums = [-1, 1, 0, -3, 3]`
Output: `[0, 0, 9, 0, 0]`
### Example 3
Input: `nums = [0, 0]`
Output: `[0, 0]`


---

## Constraints

- `2 <= nums.length <= 10⁵`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

---

## Follow-up

Can you solve the problem in `O(1)` extra space complexity?  
(Note: the output array **does not** count as extra space.)

## Solution Overview

This solution computes the product of all elements in the array except the current one by using **prefix and postfix product arrays**.

### Steps:
1. **Prefix Product Pass**  
   Build a prefix array where `prefix[i]` is the product of all elements from the start of the array up to index `i`.

2. **Postfix Product Pass**  
   Build a postfix array where `postfix[i]` is the product of all elements from index `i` to the end of the array.

3. **Final Output Computation**  
   For each index `i` in the input array:
   - If `i == 0`: result is `postfix[1]`  
   - If `i == n - 1`: result is `prefix[n - 2]`  
   - Else: result is `prefix[i - 1] * postfix[i + 1]`

This method avoids using division and works efficiently in three linear passes.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`  
  - One pass to compute prefix products  
  - One pass to compute postfix products  
  - One pass to build the result array

- **Space Complexity:** `O(n)`  
  - Additional space for prefix and postfix arrays  
  - The output array is not counted toward extra space per the problem statement

