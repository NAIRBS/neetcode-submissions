class Solution: # 12th Oct Revision
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target: 
                return middle # If it hits the target
            if nums[left] <= nums[middle]:  # Check if left half is sorted
                if nums[left] <= target < nums[middle]:
                    right = middle - 1  # Target is within left half
                else:
                    left = middle + 1   # Target is in right half
            else: # Otherwise, right half must be sorted
                if nums[middle] < target <= nums[right]:
                    left = middle + 1   # Target is within right half
                else:
                    right = middle - 1  # Target is in left half
        return -1