class Solution:
    def singleNumber(self, nums: List[int]) -> int: 
        result = 0 # XORing any number with 0 remains unchanged (x ^ 0 = x)
        for num in nums:
            result ^= num #  XORing a number by itself evaluates to 0 (x ^ x = 0), 
        return result # XOR operation is commutative and associative, the order of elements does not matter.