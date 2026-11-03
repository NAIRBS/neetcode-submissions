class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time_taken = 0
        # Go through grid, record all fresh and rotten fruits
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append((row, col)) # If rotten store coord
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]] # right, left, up , down
        while fresh > 0 and q: # While there is fresh fruits and rotten fruits
            for i in range(len(q)): # For each rotten fruit
                r, c = q.popleft()
                for delta_row, delta_col in directions: # For each direction
                    row, col = r + delta_row, c + delta_col
                    if (row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1):
                        grid[row][col] = 2 # For each node alongside the axis that has fresh fruit
                        q.append((row, col)) # Add to rotten fruit pile 
                        fresh -= 1
            time_taken += 1
        if fresh == 0:
            return time_taken
        else:
            return -1