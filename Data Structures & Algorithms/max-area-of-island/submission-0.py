class Solution: # Similar solution to number of islands
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        max_land_count = 0 # New
        curr_land_count = 0 # New
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        def dfs(row, col):
            nonlocal curr_land_count
            visited.add((row, col))
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for row_offset, col_offset in directions:
                neighbor_row = row + row_offset
                neighbor_col = col + col_offset
                # 1. Skip if the neighbor is outside the grid bounds
                if not (0 <= neighbor_row < ROWS and 0 <= neighbor_col < COLS):
                    continue
                # 2. Skip if it's water ("0") or already visited
                if grid[neighbor_row][neighbor_col] == 0 or (neighbor_row, neighbor_col) in visited:
                    continue
                # 3. Otherwise, it's valid unvisited land, time to go exploring
                curr_land_count += 1  # New
                dfs(neighbor_row, neighbor_col)
                
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    curr_land_count = 1  # New
                    dfs(row, col)
                    max_land_count = max(curr_land_count, max_land_count)  # New
        
        return max_land_count