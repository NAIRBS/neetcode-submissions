class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, middle, high = 0, len(nums)//2, len(nums)-1
        while low <= high:
            if nums[middle] == target: return middle
            if target < nums[middle]: # Search low side
                high = middle - 1
                middle = (high-low)//2 + low
            if target > nums[middle]: # Search high side
                low = middle + 1
                middle = (high-low)//2 + low
        return -1