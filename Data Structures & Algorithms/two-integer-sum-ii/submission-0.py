class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1  # Start two pointers: one at the beginning, one at the end

        while l < r:  # Keep checking while left pointer is before the right
            curSum = numbers[l] + numbers[r]  # Add the numbers at the two pointers

            if curSum > target:
                r -= 1  # If the sum is too big, move the right pointer left to get a smaller number
            elif curSum < target:
                l += 1  # If the sum is too small, move the left pointer right to get a bigger number
            else:
                return [l + 1, r + 1]  # Found the two numbers, return their positions (1-based index)
