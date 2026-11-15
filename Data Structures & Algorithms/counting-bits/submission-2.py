class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        for number in range(1, n + 1):
            if offset * 2 == number:
                offset = number
            dp[number] = 1 + dp[number - offset]
        return dp