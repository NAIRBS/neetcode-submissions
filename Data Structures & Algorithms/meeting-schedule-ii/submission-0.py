"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start) # Sort by start time
        min_heap = [] # Track earliest end time in active meetings, we only care about the EARLIEST (the min) end time!
        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start: # If current active meeting finshes in time for next meeting
                heapq.heappop(min_heap) # Pretend meeting ended, and pop current occupant
            heapq.heappush(min_heap, interval.end) # Push new endtime for the new meeting
        return len(min_heap) # Length of heap is the number of simultaneous meetings (rooms needed)