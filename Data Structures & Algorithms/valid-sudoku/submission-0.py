class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Start with rows
        for rows in range(9): 
            count = {}
            for cols in range(9): # For each value in the row
                current_val = board[rows][cols]
                if current_val != ".":
                    count[current_val] = 1 + count.get(current_val, 0)
                    if count[current_val] > 1:
                        return False
        
        # Now do cols
        for cols in range(9): 
            count = {}
            for rows in range(9): # For each value in the row
                current_val = board[rows][cols]
                if current_val != ".":
                    count[current_val] = 1 + count.get(current_val, 0)
                    if count[current_val] > 1:
                        return False
        
        # Now do 3x3 grid...? I think making a string makes the most sense.
        # Since the board must be 9x9, there should be 9 grids of 3x3
        x = 0 # Current Col
        y = 0 # Current Row
        for rows in range(3):
            for cols in range(3):
                matrix = []
                for row in range(3):
                    for col in range(3):
                        # print(y+row)
                        # print(x+col)
                        if board[y+row][x+col] != ".": 
                            matrix.append(board[y+row][x+col])
                # print(matrix)
                count = {}
                for i in range(len(matrix)):
                    count[matrix[i]] = 1 + count.get(matrix[i], 0)
                    if count[matrix[i]] > 1:
                        return False
                x += 3
            x = 0
            y += 3

        return True

        
        