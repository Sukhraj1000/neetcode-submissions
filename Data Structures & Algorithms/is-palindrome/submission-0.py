class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1  # Start two pointers at the beginning and end of the string

        while l < r:  # Keep checking characters while left is before right
            # Move left pointer until it points to a letter or digit
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # Move right pointer until it points to a letter or digit
            while r > l and not self.alphaNum(s[r]):
                r -= 1

            # Compare the characters in lowercase form
            if s[l].lower() != s[r].lower():
                return False  # Not the same, so it's not a palindrome

            # Move both pointers toward the center
            l, r = l + 1, r - 1

        return True  # All checks passed, so it is a palindrome

    def alphaNum(self, c):
        # Checks if character c is alphanumeric (a-z, A-Z, or 0-9)
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
