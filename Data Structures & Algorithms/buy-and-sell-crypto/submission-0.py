class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding Window Solution
        left, right = 0, 1 # Can't buy and sell on the same day
        max_profit = 0 # Default if no profit, return 0
        while right < len(prices): # Avoid out of bounds, cover entire search space
            if prices[left] < prices[right]: # Price on sell day higher than buy day (Profit!)
                max_profit = max(max_profit, (prices[right] - prices[left])) # Compare to prev profits
            else: left = right # If there is a new "lowest" price, set new buy price!
            right += 1 # Keep moving to the end of the list
        return max_profit

        # Dynamic programming Solution
        # max_profit = 0
        # min_buy = prices[0]
        # for price in prices:
        #     max_profit = max((price - min_buy), max_profit)
        #     min_buy = min(min_buy, price)
        # return max_profit        