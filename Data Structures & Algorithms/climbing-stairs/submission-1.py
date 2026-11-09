class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 1
        for step in range(n): # Fibonacci pattern
            first, second = first + second, first
        return second