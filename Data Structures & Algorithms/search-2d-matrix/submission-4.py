class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Non-decreasing, either ascending or duplicate of numbers going left to right
        # Let's do binary search on each row?

        # for row in range(len(matrix)):
        #     left, middle, right = 0, len(matrix[0])//2, len(matrix[0])-1
        #     if len(matrix[row]) <= 3:
        #         if matrix[row][right] == target: return True
        #         if matrix[row][middle] == target: return True
        #         if matrix[row][left] == target: return True
        #         continue
        #     while left < right:
        #         if target > matrix[row][right]: break # Skip the entire row if target larger
        #         if matrix[row][right] == target: return True
        #         if matrix[row][middle] == target: return True
        #         if matrix[row][left] == target: return True
        #         if target > matrix[row][middle]:
        #             left = middle + 1
        #             middle = (right-left)//2
        #         if target < matrix[row][middle]:
        #             right = middle - 1
        #             middle = (right-left)//2
        # return False
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1

        while top <= bot: # Do a binary search across ROWS
            row = (top + bot)//2
            if target > matrix[row][-1]: # Check the END of each row
                top = row + 1
            elif target < matrix[row][0]: # Check the START of each row
                bot =  row - 1
            else: # If target within RANGE of the row, you've probably found the closest row to the target
                break 
        
        if not (top <= bot): return False # If we broke the while loop, but rows did not contain target value
        row = (top + bot)//2
        left, right = 0, cols - 1
        while left <= right:
            # middle = (left + right) // 2 # Always finds the middle, both this line and the following work btw
            middle = (right - left)//2 + left 
            if target > matrix[row][middle]: # If more than middle, search right
                left = middle + 1
            elif target < matrix[row][middle]: # If less than middle, search left
                right = middle - 1
            else: # If not more or less means equal, so target was found in the middle
                return True
        return False
