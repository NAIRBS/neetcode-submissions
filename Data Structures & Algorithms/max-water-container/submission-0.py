class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        highest_vol = 0
        while left < right:
            curr_vol = (right-left) * min(heights[left],heights[right])
            if curr_vol > highest_vol:
                highest_vol = curr_vol
            if heights[right] > heights[left]: left += 1
            elif heights[left] > heights[right]: right -= 1
            elif heights[left] == heights[right]: left += 1
        return highest_vol

