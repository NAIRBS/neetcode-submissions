class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                threesum = nums[i] + nums[left] + nums[right]
                if threesum > 0: right -= 1
                elif threesum < 0: left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1 
                    right -= 1
                    while nums[left] == nums[left-1] and left < right: 
                        left += 1
        return result