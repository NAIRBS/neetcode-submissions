class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            # 1. Add without carrying
            sum_without_carry = (a ^ b) & MASK
            
            # 2. Calculate the carry and shift it left
            carry = ((a & b) << 1) & MASK
            
            # 3. Set a to the sum and b to the carry, then repeat
            a, b = sum_without_carry, carry
            
        # Convert back if the result is a negative number in 32-bit binary
        return a if a <= MAX_INT else ~(a ^ MASK)