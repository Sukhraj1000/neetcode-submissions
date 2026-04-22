class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary to count frequency of each number
        count = {}
        # Create a list of empty lists to use as "buckets"
        # Each index i of `freq` will store numbers that appear exactly i times
        # Maximum frequency any number can have is len(nums), hence (len(nums) + 1)
        freq = [[] for n in range(len(nums)+1)]
        # First pass: count how many times each number appears
        for n in nums:
            count[n] = 1+ count.get(n,0)

        # Second pass: group numbers by their frequency
        # e.g., if number 3 appears 2 times, it goes into freq[2]
        for n,c in count.items():
            freq[c].append(n)

        # Prepare the result list
        res = []
        # Iterate over the frequency list in reverse (from high freq to low)
        for i in range(len(freq) -1, 0, -1):
            # For each number that has this frequency
            for n in freq[i]:
                # Append the number to the result list
                res.append(n)

                # Once we have k elements, return the result
                if len(res) ==k:
                    return res
