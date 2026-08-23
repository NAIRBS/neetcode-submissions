class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # We could find the gap then repair the array?
        # If complexity of that is log(n) and another binary search is the same then
        # Complexity of this would be 2log(n), reduced down to log(n) still?
        # But there has to be a better way to do this...?

        # if len(nums) <= 3:
        #     for i in range(len(nums)):
        #         if nums[i] == target:
        #             return i
        #     return -1

        # min_val = 1000
        # min_index = 0
        # left, right = 0, len(nums)-1
        # while left <= right:
        #     if nums[left] < nums[right]: # Right should be more than left is consec, return left
        #         #min_val = min(min_val, nums[left])
        #         min_val, min_index = min((min_val, min_index), (nums[left], left))
        #         break
        #     middle = (left + right) // 2
        #     #min_val = min(min_val, nums[middle])
        #     min_val, min_index = min((min_val, min_index), (nums[middle], middle))
        #     if nums[middle] >= nums[left]: left = middle + 1 # If gap found on right
        #     else: right = middle - 1 # If gap found on left
        # print(min_index)
        # nums = nums[min_index:len(nums)] + nums[0:min_index]
        # print(nums)

        # # Now we just do normal binary search I guess
        # left, right = 0, len(nums)-1
        # while left <= right:
        #     middle = (left + right) // 2
        #     if nums[middle] > target: # Search the left side
        #         right = middle - 1
        #     elif nums[middle] < target: # Search the right side
        #         left = middle + 1
        #     else: 
        #         result = middle + min_index
        #         if result > len(nums) - 1: result -= (len(nums))
        #         return result # Remember to adjust for the previous rotation
        # return -1

        # Model Answer
        left, right = 0, len(nums)-1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target: return middle # If it hit the target on the head
            if nums[left] <= nums[middle]: # If the LEFT side is sorted
                if nums[left] <= target < nums[middle]: # Check if target lies within the sorted left half
                    right = middle - 1  # Search left
                else:
                    left = middle + 1  # Search right as target is in the jumbled up right side
            else: # If the RIGHT side is sorted
                if nums[middle] < target <= nums[right]: # Check if target lies within the sorted right half
                    left = middle + 1  # Search right
                else:
                    right = middle - 1  # Search left as target is in the jumbled up left side
        return -1