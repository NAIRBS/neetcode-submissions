class Solution: # 11th Oct Revision
    def findMin(self, nums: List[int]) -> int:
        left, middle, right = 0, len(nums)//2, len(nums) - 1
        while left < right:
            if nums[middle] > nums[right]:
                left = middle + 1
            else: 
                right = middle
            middle = (left + right) // 2
        return nums[left]