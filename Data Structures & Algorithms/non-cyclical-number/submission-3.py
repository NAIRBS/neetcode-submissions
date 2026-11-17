class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumsquares(n)
        while slow != fast:
            fast = self.sumsquares(fast)
            fast = self.sumsquares(fast)
            slow = self.sumsquares(slow)
        return True if fast == 1 else False

    def sumsquares(self, n:int) -> int:
        output = 0
        while n:
            output += (n % 10) ** 2
            n //= 10
        return output