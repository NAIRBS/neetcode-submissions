class Solution:
    def isHappy(self, n: int) -> bool:
        prev_value = set()
        current_sum = 0
        while 1:
            while n > 0:
                current_sum += (n % 10) ** 2
                n //= 10
            if current_sum == 1:
                return True
            elif current_sum in prev_value:
                return False
            else:
                prev_value.add(current_sum)
            n = current_sum
            current_sum = 0