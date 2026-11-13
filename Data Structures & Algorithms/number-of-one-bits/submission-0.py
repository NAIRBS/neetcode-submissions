class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32, -1, -1):
            if n >= (2**i):
                n -= 2**i
                count += 1
        return count