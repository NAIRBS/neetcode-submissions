class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            remainder = target - nums[i]
            for j in range(len(nums)):
                if i == j: continue
                if nums[j] == remainder:
                    if i > j: return [j,i]
                    else: return [i,j]
        