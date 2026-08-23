class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 111100000 or 1111000111 or 00000011111  
        # We can make the assumption that in between TWO elements, there is a HUGE difference
        # That the number suddenly goes DOWN instead of up, the diff is negative
        # Let's use that to search the array, we need to find this gap, after which we just return the left side
        
        # left, right = 0, len(nums)-1
        # min_val = 1000
        # if len(nums) <= 3: return min(nums)
        # while left < right: # All are unique elements
        #     middle = (right - left)//2 + left
        #     if right - left == 1: 
        #         min_val = min(nums[left], nums[middle], nums[right], min_val)
        #         break
        #     if nums[left] > nums[middle]: # Gap found on left side
        #         right = middle - 1
        #         min_val = min(nums[left], nums[middle], nums[right], min_val)
        #     elif nums[right] < nums[middle]: # Gap found on right side
        #         left = middle + 1
        #         min_val = min(nums[left], nums[middle], nums[right], min_val)
        #     else: return nums[left] # Means that for the ENTIRE L > M > R, its in consecutive order already
        # return min_val

        # The model answer
        min_val = 1000
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] < nums[right]: # Right should be more than left is consec, return left
                min_val = min(min_val, nums[left])
                break
            middle = (left + right) // 2
            min_val = min(min_val, nums[middle])
            if nums[middle] >= nums[left]: left = middle + 1 # If gap found on right
            else: right = middle - 1 # If gap found on left
        return min_val



            

