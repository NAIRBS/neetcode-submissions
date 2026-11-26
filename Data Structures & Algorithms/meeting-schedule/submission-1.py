"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start) # Sort it by start time
        for i in range(1, len(intervals)):
            if intervals[i - 1].end > intervals[i].start:
                return False # If the previous end time overlaps next session start time
        return True