class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output, prefix, postfix = [], 1, 1 # Easier solution
        # for i in range(len(nums)):
        #     output.append(prefix)
        #     prefix *= nums[i]
        # for i in range(len(nums) - 1, -1, -1):
        #     output[i] *= postfix
        #     postfix *= nums[i]
        # return output
        n, output, prefix, postfix = len(nums), [1] * len(nums), 1, 1
        for i in range(n): # One pass solution
            output[i] *= prefix # Forward pass (Prefix)
            prefix *= nums[i]
            j = n - 1 - i # Backward pass (Postfix)
            output[j] *= postfix
            postfix *= nums[j]        
        return output     