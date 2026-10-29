class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Track where queens are already placed so we don't attack each other
        cols_used = set()
        pos_diags = set()  # (row + col) for diagonals going /
        neg_diags = set()  # (row - col) for diagonals going \

        result = []
        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            # Base Case: If we successfully placed queens in all rows, save the board
            if row == n:
                result.append(["".join(r) for r in board])
                return

            # Try placing a queen in each column of the current row
            for col in range(n):
                # Check if this position is under attack by another queen
                if col in cols_used or (row + col) in pos_diags or (row - col) in neg_diags:
                    continue  # Skip this spot, it's unsafe!

                # 1. PLACE the queen
                cols_used.add(col)
                pos_diags.add(row + col)
                neg_diags.add(row - col)
                board[row][col] = "Q"

                # 2. RECURSE to the next row
                backtrack(row + 1)

                # 3. REMOVE the queen (Backtrack / undo our choice to try other paths)
                cols_used.remove(col)
                pos_diags.remove(row + col)
                neg_diags.remove(row - col)
                board[row][col] = "."

        backtrack(0)
        return result