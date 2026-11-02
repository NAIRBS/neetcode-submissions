class Solution: # Use multi source BFS
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
    
        def addCell(row, col): # Check cell out of bounds, visited, or is a wall
            if (min(row, col) < 0 or row == ROWS or col == COLS or (row,col) in visited or grid[row][col] == -1):
                return 
            visited.add((row, col)) # Mark visited
            q.append([row, col]) # Add neighbour coords to queue for future processing

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0: # Find all treasure chests
                    q.append([row, col]) # Add to queue
                    visited.add((row, col)) # Mark treasure chest as visited
        dist = 0 # Find chests first then explore dist 1, 2, etc from chests, like radar
        while q: # While there are cells in the queue
            for i in range(len(q)):
                row, col = q.popleft() # Remove coords
                grid[row][col] = dist # Upgrade with shortest dist
                addCell(row + 1, col) # Check below
                addCell(row - 1, col) # Check above
                addCell(row, col + 1) # Check right
                addCell(row, col - 1) # Check left
            dist += 1 # Increment 1 after full level dfs traversal