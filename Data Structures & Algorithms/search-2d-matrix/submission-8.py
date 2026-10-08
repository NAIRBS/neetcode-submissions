class Solution: # Better solution O(log(m*n)) time intead of O(m·log n) searching through each row
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            # map the 1-D index back to 2-D
            row = mid // n
            col = mid % n
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False