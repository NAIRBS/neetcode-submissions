class MedianFinder:

    def __init__(self):
        self.small = [] # min heap for smaller half (stored as negative int)
        self.large = [] # max heap for larger half 

    def addNum(self, num: int) -> None:
        # 1. Always push to max-heap first
        heapq.heappush(self.small, -num)
        # 2. Ensure every element in small is <= every element in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # 3. Balance the sizes (small can have at most 1 more element than large)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0
        