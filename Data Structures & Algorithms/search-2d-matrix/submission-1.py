class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Non-decreasing, either ascending or duplicate of numbers going left to right
        # Let's do binary search on each row?
        for row in range(len(matrix)):
            left, middle, right = 0, len(matrix[0])//2, len(matrix[0])-1
            if len(matrix[row]) <= 3:
                if matrix[row][right] == target: return True
                if matrix[row][middle] == target: return True
                if matrix[row][left] == target: return True
                continue
            while left < right:
                if target > matrix[row][right]: break # Skip the entire row if target larger
                if matrix[row][right] == target: return True
                if matrix[row][middle] == target: return True
                if matrix[row][left] == target: return True
                if target > matrix[row][middle]:
                    left = middle + 1
                    middle = (right-left)//2
                if target < matrix[row][middle]:
                    right = middle - 1
                    middle = (right-left)//2
        return False