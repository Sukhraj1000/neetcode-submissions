class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty dictionary to store numbers we have seen so far,
        # mapping each number to its index in the list
        prevMap = {}

        # Iterate through the list of numbers using both index (i) and value (n)
        for i, n in enumerate(nums):
            # Calculate the difference between the target and the current number
            # This is the number we want to find in the dictionary
            diff = target - n

            # Check if the required complement (diff) exists in the dictionary
            # If it does, we found two numbers (n and diff) whose sum is the target
            if diff in prevMap:
                # Return the indices of the two numbers
                return [prevMap[diff], i]

            # If the complement is not found, store the current number and its index
            # so we can use it to check for future pairs
            prevMap[n] = i
