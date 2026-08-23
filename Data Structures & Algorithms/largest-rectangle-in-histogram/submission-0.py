class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair: (index, height)
        for i, h in enumerate(heights):
            start = i
            # While stack not empty + top of stack height is MORE than current height
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea =  max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        # At the end of going through all indexes, just find the maxArea of whatever is left in the stack
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea