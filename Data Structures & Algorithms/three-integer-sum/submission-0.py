class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []  # This will hold all the unique triplets
        nums.sort()  #  Must call the sort function with parentheses to actually sort the list

        for i, a in enumerate(nums):
            # Skip duplicate values for the first number
            if i > 0 and a == nums[i - 1]:
                continue

            # Set up two pointers for the remaining part of the list
            l, r = i + 1, len(nums) - 1

            while l < r:
                curSum = a + nums[l] + nums[r]  # Calculate current sum of the triplet

                if curSum > 0:
                    r -= 1  # Too big → move right pointer to the left
                elif curSum < 0:
                    l += 1  # Too small → move left pointer to the right
                else:
                    res.append([a, nums[l], nums[r]])  # Found a valid triplet
                    l += 1

                    # Skip duplicates for the second number
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res  # Return the list of triplets
