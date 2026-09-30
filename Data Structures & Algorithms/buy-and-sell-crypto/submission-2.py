class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, maxprofit = 0, 1, 0
        while right < len(prices): # While right window within search space
            if prices[left] < prices[right]: # Calculate current maxprofit
                maxprofit = max(maxprofit, (prices[right] - prices[left]))
            else:
                left = right # If right < left, should replace buying price
            right += 1 # Still need to keep expanding window
        return maxprofit 