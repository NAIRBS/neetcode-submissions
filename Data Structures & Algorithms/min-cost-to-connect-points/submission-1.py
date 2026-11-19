class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, node = len(points), 0
        dist = [100000000] * n # Min cost to connect i to MST
        visit = [False] * n # Track if point visited
        edges, min_cost = 0, 0
        while edges < n - 1: # Keep going until max number of possible edges
            visit[node] = True # Mark node as visited
            nextNode = -1
            for i in range(n):
                if visit[i]: continue # Exclude visited points
                currDist = (abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1])) 
                dist[i] = min(dist[i], currDist) # Update whichever one is min_dist
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i
            min_cost += dist[nextNode] # Add to min_cost after updating all costs
            node = nextNode # "Move" to next node
            edges += 1 # Increment edge count
        return min_cost