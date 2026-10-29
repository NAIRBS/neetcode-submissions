class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(row: int, col: int, index: int) -> bool:
            if index == len(word):
                return True # Finished finding entire word
            if not (0 <= row < ROWS and 0 <= col < COLS) or board[row][col] != word[index]:
                return False # Out of bounds
            # Temporarily mark as visited and explore neighbors
            temp, board[row][col] = board[row][col], '#'
            found = any(
                dfs(next_row, next_col, index + 1) 
                for next_row, next_col in (
                    (row + 1, col), 
                    (row - 1, col), 
                    (row, col + 1), 
                    (row, col - 1)
                )
            )
            board[row][col] = temp  # Backtrack
            return found

        return any(
            dfs(row, col, 0) 
            for row in range(ROWS) 
            for col in range(COLS)
        )