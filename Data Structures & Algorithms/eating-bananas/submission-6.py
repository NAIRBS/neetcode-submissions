class Solution: # 10th Oct Revision
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles) # Lowest k = 1, highest k = biggest pile
        result = high # Set highest first so it can be reduced later
        while low <= high:
            hours_to_finish_bananas = 0
            banana_per_hour = (low + high) // 2
            for pile in piles: # Calculate h value
                hours_to_finish_bananas += math.ceil(pile/banana_per_hour)
            if hours_to_finish_bananas <= h:  # If its within range (below desired h)
                high = banana_per_hour - 1
                result = min(result, banana_per_hour) # Save whichever one is lower
            else:
                low = banana_per_hour + 1
        return result