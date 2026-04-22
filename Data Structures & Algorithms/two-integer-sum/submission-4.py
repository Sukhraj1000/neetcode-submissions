class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i] # prevmap[diff] gives us index of number we saw, 'i' is the number we're on
            prevMap[n] = i # update hm with the diff value that wasnt found