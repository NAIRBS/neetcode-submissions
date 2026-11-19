class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        min_heap = [(0, 0)] # Stores cost: points_index
        total_cost = 0

        while len(visited) < len(points):
            cost, curr_index = heapq.heappop(min_heap)
            if curr_index in visited: continue
            visited.add(curr_index)
            total_cost += cost

            x1, y1 = points[curr_index]
            for index in range(len(points)):
                if index not in visited:
                    dist = abs(x1 - points[index][0]) + abs(y1 - points[index][1])
                    heapq.heappush(min_heap, (dist, index))
        return total_cost