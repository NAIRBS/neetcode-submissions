class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n # Initialize the minimum cost to reach every city (0 to n-1) as infinity.
        prices[src] = 0 # Cost to reach the starting city from itself is 0.
        # Allow up to (k + 1) edges/flights since k stops means at most k + 1 flights.
        for i in range(k + 1):
            # Copy current shortest prices so updates in this iteration don't cascade
            # within the same flight step (preventing using more than i+1 flights).
            temp_prices = prices.copy()
            for s, d, p in flights:  # s = source, d = destination, p = price
                # Skip if we haven't found a valid path to the source city yet.
                if prices[s] == float("inf"):
                    continue
                # Relax the edge: if taking this flight gives a cheaper total cost
                # to city `d` than what we had in `temp_prices`, record it.
                if (prices[s] + p) < temp_prices[d]:
                    temp_prices[d] = prices[s] + p
            # Commit the updated costs after completing this flight round.
            prices = temp_prices
        # If `dst` is still unreachable within k stops, return -1; otherwise return the min cost.
        return -1 if prices[dst] == float("inf") else prices[dst]