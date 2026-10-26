class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num) # Negated values for max-heap
        for i in range (k-1): # Push out until juuust before the last one
            heapq.heappop(heap)
        return -heapq.heappop(heap)