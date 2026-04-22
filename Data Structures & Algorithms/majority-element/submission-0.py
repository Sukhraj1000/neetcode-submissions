class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        res, maxCount = 0, 0
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            if freq[n] >  maxCount:
                res = n
            else:
                res
            maxCount = max(freq[n], maxCount)
        return res

        
        