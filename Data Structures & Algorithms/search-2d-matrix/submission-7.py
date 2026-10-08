class Solution: # 9th Oct Revision
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, middle, right = 0, (len(matrix[0]))//2, len(matrix[0])-1
        for row in range(len(matrix)):
            if target >= matrix[row][left] and target <= matrix[row][right]:
                while left <= right:
                    if target > matrix[row][middle]:
                        left = middle + 1
                    elif target < matrix[row][middle]:
                        right = middle - 1
                    else:
                        return True
                    middle = (right - left)//2 + left
        return False