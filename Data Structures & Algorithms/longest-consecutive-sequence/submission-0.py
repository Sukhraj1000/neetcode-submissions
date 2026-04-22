class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)  # Convert the list to a set to remove duplicates and allow fast lookups
        longest = 0    # This will store the length of the longest consecutive sequence found

        for n in nums:  # Go through every number in the original list
            # Check if this number could be the start of a sequence
            # If (n - 1) is NOT in the set, that means n is the beginning of a sequence
            if (n - 1) not in s:
                length = 0  # Start counting the length of this new sequence

                # Keep checking the next number (n + length) while it's in the set
                while (n + length) in s:
                    length += 1  # Sequence continues, increase the count

                    # Update the longest sequence if this one is longer
                    longest = max(longest, length)

        return longest  # Return the longest sequence length found