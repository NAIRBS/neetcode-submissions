class Solution: # Cleaned up a little bit
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        max_land_count = 0

        def dfs(row, col):
            visited.add((row, col))
            area = 1
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for row_offset, col_offset in directions:
                neighbor_row = row + row_offset
                neighbor_col = col + col_offset
                # 1. Skip if the neighbor is outside the grid bounds
                if (0 <= neighbor_row < ROWS and 0 <= neighbor_col < COLS and 
                    grid[neighbor_row][neighbor_col] == 1 and 
                    (neighbor_row, neighbor_col) not in visited):
                    area += dfs(neighbor_row, neighbor_col)
            return area
                
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    max_land_count = max(max_land_count, dfs(row, col))  # New
        
        return max_land_count