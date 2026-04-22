class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # hashmap
        freq = [[] for i in range(len(nums) + 1)] # set the empty array with how many indices in input

        for n in nums: # loop through input
            count[n] = 1 + count.get(n, 0) # increment count in HM, if no number set '0'
        for n, c in count.items(): # getting the whole HM
            freq[c].append(n) # appending the values of keys to freq
        
        res = [] # empty array for result
        for i in range(len(freq) -1, 0, -1): # start i at end of array(-1) to 0 index as decrementing(-1)
            for n in freq[i]: # loop through highest freq 
                res.append(n) # append to array
                if len(res) == k: # does it match number of k
                    return res