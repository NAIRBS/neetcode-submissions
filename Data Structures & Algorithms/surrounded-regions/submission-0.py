class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1,0), (0, 1), (0, -1)]
        # We can just do DFS on every "O" found on the edges
        # and mark it as T, we can then go through every adj coord and make it T
        # After that convert all T -> O and all O -> X
        
        def bfs(row, col):
            queue = deque([(row,col)])
            board[row][col] = "T" # Mark border connected as "Safe" with "T" temporarily
            while queue:
                row, col = queue.popleft()
                for delta_row, delta_col in directions:
                    new_row, new_col = row + delta_row, col + delta_col
                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and board[new_row][new_col] == "O":
                        board[new_row][new_col] = "T"
                        queue.append((new_row, new_col))

        for row in range(ROWS):
            if board[row][0] == "O":
                bfs(row, 0)
            if board[row][COLS-1] == "O":
                bfs(row, COLS-1) 
        for col in range(COLS):
            if board[0][col] == "O":
                bfs(0, col)
            if board[ROWS-1][col] == "O":
                bfs(ROWS-1, col)
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "T":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"
        return