class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {} # 1. Build the Trie
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, {})
            node["$"] = word  # Store the full word at the end node
        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(row, col, parent):
            char = board[row][col]
            curr = parent[char]         
            # If we found a word, add it to results and remove it to avoid duplicates
            if "$" in curr:
                res.append(curr.pop("$"))
            # Mark cell as visited
            board[row][col] = "#"
            # Explore 4 directions
            for delta_row, delta_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + delta_row, col + delta_col
                if 0 <= new_row < ROWS and 0 <= new_col < COLS and board[new_row][new_col] in curr:
                    dfs(new_row, new_col, curr)
            # Restore cell
            board[row][col] = char
            # Optimization: Prune empty Trie branches to speed up future searches
            if not curr:
                parent.pop(char)
        # 2. Start DFS from every cell on the board
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] in root:
                    dfs(row, col, root)
        return res