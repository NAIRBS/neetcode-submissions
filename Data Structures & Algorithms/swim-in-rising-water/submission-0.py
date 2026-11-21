class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit.add((0, 0))
        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return t
            for delta_row, delta_col in directions:
                next_index_row, next_index_col = r + delta_row, c + delta_col
                if (not (0 <= next_index_row < N) or not (0 <= next_index_col < N) or (next_index_row, next_index_col) in visit):
                    continue
                visit.add((next_index_row, next_index_col))
                heapq.heappush(minH, [max(t, grid[next_index_row][next_index_col]), next_index_row, next_index_col])