class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Dictionary to count frequency of characters in the current window
        count = {}

        # Result to store the length of the longest valid window
        res = 0

        # Left pointer of the sliding window
        l = 0

        # Variable to keep track of the count of the most frequent character in the current window
        maxf = 0

        # Right pointer iterates through the string
        for r in range(len(s)):
            # Increment the count of the current character
            count[s[r]] = 1 + count.get(s[r], 0)

            # Update the most frequent character count in the current window
            maxf = max(maxf, count[s[r]])

            # If the number of characters we need to replace > k, shrink the window from the left
            # (r - l + 1) is the size of the window
            # If window size - max frequency > k → more than k replacements needed → shrink window
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1  # Remove the leftmost character from the count
                l += 1            # Shrink the window

            # Update the result with the current window length if it's the largest so far
            res = max(res, r - l + 1)

        # Return the length of the longest substring that can be made uniform with at most k changes
        return res
