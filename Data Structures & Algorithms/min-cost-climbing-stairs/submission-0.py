class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Append 0 to represent the top of the floor beyond the last step
        cost.append(0)
        
        # Iterate backwards from the third-to-last step down to 0
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
            
        # The minimum cost to reach the top will be the min of starting at index 0 or 1
        return min(cost[0], cost[1])