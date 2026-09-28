class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Simply put, find the lowest on the left and the highest on the right
        left, right, max_profit = 0, 1, 0 # Sliding window approach
        while right < len(prices): # While right window within range
            if prices[left] < prices[right]: # If profit to be made, calc it
                max_profit = max(max_profit, (prices[right] - prices[left]))
            else:
                left = right # Else start of a new window
            right += 1 # Regardless of start or curr window, expand the window
        return max_profit