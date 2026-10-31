class Solution: # Model Answer
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        def dfs(row, col):
            # Base case: check bounds and if cell is water (0)
            if not (0 <= row < ROWS and 0 <= col < COLS) or grid[row][col] == 0:
                return 0
            
            # Mark the cell as visited by changing it to 0
            grid[row][col] = 0
            
            # Current cell counts as 1, plus recursively check all 4 directions
            return (1 + dfs(row - 1, col) + 
                        dfs(row + 1, col) + 
                        dfs(row, col - 1) + 
                        dfs(row, col + 1))
                
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))
        
        return max_area