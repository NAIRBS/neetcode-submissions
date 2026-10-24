class Solution: # Naive Solution
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) >= 2:
            if stones[-1] == stones[-2]:
                stones = stones[:-2]
            else:
                diff = stones[-1] - stones[-2]
                stones = stones[:-2]
                stones.append(diff)
                stones.sort()
        return stones[0] if stones else 0