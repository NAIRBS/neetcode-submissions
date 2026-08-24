class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Naive solution that somehow passed?
        # nums = nums1 + nums2
        # nums.sort()
        # if len(nums)%2 == 0:
        #     return (nums[(len(nums)-1)//2] + nums[((len(nums)-1)//2)+1])/2
        # return nums[(len(nums)-1)//2]
        
        # Model Answer
        if len(nums2) < len(nums1):  # Code below assumes nums2 is LARGER/EQUAL than nums1, so rearrange it
            nums1, nums2 = nums2, nums1

        left, right = 0, len(nums1) - 1
        middle = (len(nums1) + len(nums2)) // 2
        # We try to find the individual paritions of both lists, when added together creates a sorted partition
        # The idea is to find the "correct" partition for BOTH lists, and use partition heads to find median
        while True:
            i = (left + right) // 2 # Find midpoint of nums1
            j = middle - i - 2 # Find the adjusted midpoint of nums2, -2 cause array start from 0 and 2 arrays etc
            # Basic bounds checking for the dual binary search
            num1_left = nums1[i] if i >= 0 else float("-infinity")
            num1_right = nums1[i + 1] if (i + 1) < len(nums1) else float("infinity")
            num2_left = nums2[j] if j >= 0 else float("-infinity")
            num2_right = nums2[j + 1] if (j + 1) < len(nums2) else float("infinity")
            # To find if partitions in both lists are correct, check if lists separation fits each other
            if num1_left <= num2_right and num2_left <= num1_right:
                if (len(nums1) + len(nums2)) % 2: # If length of combined list is ODD (returns 1)
                    return min(num1_right, num2_right) # Just return whichever one is smaller
                return (max(num1_left, num2_left) + min(num1_right, num2_right)) / 2 # Else return even median
            elif num1_left > num2_right: # Binary search baby letsgo
                right = i - 1
            else:
                left = i + 1