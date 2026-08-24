class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums)%2 == 0:
            return (nums[(len(nums)-1)//2] + nums[((len(nums)-1)//2)+1])/2
        return nums[(len(nums)-1)//2]
        # left, right = 0, len(nums)-1
        # while left <= right:
        #     middle = (left + right) // 2
        #     if middle 