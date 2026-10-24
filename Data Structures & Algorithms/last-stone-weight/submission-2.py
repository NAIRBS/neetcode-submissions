class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] # Create min heap and negate all weights
        heapq.heapify(stones) 

        while len(stones) > 1: 
            first, second = heapq.heappop(stones), heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0) # Handles edge case of no stones
        return abs(stones[0]) # The "largest" value is also the smallest weight!