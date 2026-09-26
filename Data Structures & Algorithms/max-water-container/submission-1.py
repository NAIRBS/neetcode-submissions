class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        left, right = 0, len(heights) - 1
        while left < right:
            curr_vol = (right - left) * min(heights[left], heights[right])
            max_vol = max(max_vol, curr_vol)
            if heights[right] > heights[left]: left += 1
            elif heights[left] > heights[right]: right -= 1
            else: left += 1
        return max_vol