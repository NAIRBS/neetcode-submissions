class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1,0), (0, 1), (0, -1)]
        pacific = [[False] * COLS for _ in range(ROWS)] # Track each cell can reach pacific
        atlantic = [[False] * COLS for _ in range(ROWS)] # Track each cell can reach atlantic

        def bfs(source, ocean):
            q = deque(source)
            for r, c in source: # If already adjacent to edges, it can alr reach ocean!
                ocean[r][c] = True
            while q:
                row, col = q.popleft()
                for delta_row, delta_col in directions: # For each direction, compute new coordinates
                    new_row, new_col = row + delta_row, col + delta_col
                    if (0 <= new_row < ROWS and # If new_row within bounds
                    0 <= new_col < COLS and # If new_col within bounds
                    not ocean[new_row][new_col] and  # If node has not been visited yet (marked False)
                    heights[new_row][new_col] >= heights[row][col]): # If the new row is more or equal prev row (we start from the edges in)
                        ocean[new_row][new_col] = True # Mark as that row is able to reach the ocean!
                        q.append((new_row, new_col)) # Add it to the queue

        pacific_iter, atlantic_iter = set(), set() # Set handles overlapping corners (top-left/bottom-right)
        for col in range(COLS):
            pacific_iter.add((0, col)) # Add left edge (pacific)
            atlantic_iter.add((ROWS - 1, col)) # Add right edge (Atlantic)
        for row in range(ROWS):
            pacific_iter.add((row, 0)) # Add top edge (pacific)
            atlantic_iter.add((row, COLS - 1)) # Add bottom edge (pacific)

        bfs(pacific_iter, pacific)
        bfs(atlantic_iter, atlantic)

        result = []
        for row in range(ROWS):
            for col in range(COLS):
                if pacific[row][col] and atlantic[row][col]:
                    result.append([row, col]) # Find intersection of the two sets to return
        return result