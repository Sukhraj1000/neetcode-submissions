from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary that maps a key (based on character counts) to a list of words (anagrams)
        # Using defaultdict so we don't need to check if a key already exists before appending
        anagrams_dict = defaultdict(list)

        # Iterate through each string in the input list
        for s in strs:
            # Initialize a list of 26 zeros to count occurrences of each character (a-z)
            # This acts like a signature or fingerprint for the anagram group
            count = [0] * 26

            # For each character in the current string, increment the corresponding index
            # e.g., 'a' → index 0, 'b' → index 1, ..., 'z' → index 25
            for c in s:
                count[ord(c) - ord('a')] += 1

            # Convert the list to a tuple so it can be used as a dictionary key (lists aren't hashable)
            key = tuple(count)

            # Append the current word to the list of anagrams that share the same character count signature
            anagrams_dict[key].append(s)

        # Return the list of grouped anagrams (just the values of the dictionary)
        return list(anagrams_dict.values())
