class Solution: # 7th Oct Revision
    def search(self, nums: List[int], target: int) -> int:
        left, middle, right = 0, len(nums)//2, len(nums) - 1
        while left <= right:
            if target > nums[middle]:
                left = middle + 1
                middle = (right - left)//2 + left
            elif target < nums[middle]:
                right = middle - 1
                middle = (right - left)//2 + left
            else:
                return middle
        return -1