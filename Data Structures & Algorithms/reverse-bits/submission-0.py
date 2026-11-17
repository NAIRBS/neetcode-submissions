class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            current = (n >> i) & 1
            result += (current << (31-i))
        return result