class Solution:
    def climbStairs(self, n: int) -> int:
        # These represent the number of ways to reach the top from the last step (1 way)
        # and the step before that (1 way). Think of base cases:
        # If n = 1 → 1 way, n = 2 → 2 ways (1+1 or 2)
        one, two = 1, 1

        # Loop from step n-1 down to 1 (we already know the last two cases)
        for i in range(n - 1):
            tmp = one           # Temporarily store the value of `one`
            one = one + two     # The total ways from current step = one + two
            two = tmp           # Shift `two` forward to the previous `one`
        
        # After the loop, `one` holds the number of distinct ways to climb `n` stairs
        return one
