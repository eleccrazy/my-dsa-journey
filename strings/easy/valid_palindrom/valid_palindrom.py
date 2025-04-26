def isPalindrome(self, s: str) -> bool:
    """
    Checks if the given string is a valid palindrome after removing
    non-alphanumeric characters and ignoring case.

    This solution uses a two-pointer technique after cleaning the input string.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Using two pointer technique
    s_cleaned = "".join(x.lower() for x in s if x.isalnum())

    left = 0
    right = len(s_cleaned) - 1

    while left < right:
        if s_cleaned[left] != s_cleaned[right]:
            return False
        left += 1
        right -= 1

    return True

    # Alternative shorter solution (Pythonic way):
    # return s_cleaned == s_cleaned[::-1] # Same time and space complexity as the above solution
