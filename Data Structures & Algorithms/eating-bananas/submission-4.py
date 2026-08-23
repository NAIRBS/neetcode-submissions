class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h = hours, k = rate, bananas = each pile added up
        # bananas/k = h >> bananas = kh >> k = bananas/h
        # Find min(k) for bananas/h
        # Let's do a rough best estimate guess, assuming that each pile takes only ONE hour
        # h = len(piles) >> k = max(piles[x]), so k would be the highest number of any pile

        # My attempt
        # k = 1 # Minimum has to at least be 1
        # max_k = max(piles) # It never needs to be higher than the largest pile of bananas

        # if h == len(piles): return max_k # Fastest possible time to finish the piles
        # piles.sort() # should be safe to sort it, binary search needs it sorted anyway
        # # Let's do a binary search, the search space is for each piles, we play with variable m = max_k
        # low, high = 1, max_k
        # last_middle = 0
        # while low <= high:
        #     middle = (high - low)//2 + low
        #     calc_h = 0
        #     for pile in piles:
        #         calc_h += math.ceil(pile / middle)
        #     if calc_h > h: # Takes too long, needs higher rate == lower time taken
        #         low = middle + 1
        #     elif calc_h < h: # Rate is too high, needs to try to approach h
        #         high = middle - 1
        #         last_middle = middle # We store the last found best result just in case we overshoot optimization
        #     else: # If calc_h == h, we're still not done I think, we need to converge into the best result
        #         high = middle - 1
        #         last_middle = middle
        # print("broke out")
        # return last_middle

        # Model answer
        low, high = 1, max(piles) # Lowest k = 1, highest k = biggest pile
        result = high # Set highest first so it can be reduced later
        while low <= high:
            calc_h = 0
            k = (low + high) // 2
            for pile in piles: # Calculate h value
                calc_h += math.ceil(pile/k)
            if calc_h <= h: # If its within range (below desired h)
                high = k - 1
                result = min(result, k) # Save whichever one is lower
            else:
                low = k + 1
        return result