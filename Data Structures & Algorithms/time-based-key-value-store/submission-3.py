from bisect import bisect_right
class TimeMap: # 14th Oct Revision

    def __init__(self):
        self.timestamps = {}
        self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamps:
            self.timestamps[key] = []
            self.values[key] = []
        self.timestamps[key].append(timestamp)
        self.values[key].append(value) # Store as (timestamp, value) so we can easily search by timestamp

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamps: return ""
        # finds the insertion point, bisect_right does binary search under the hood
        index = bisect_right(self.timestamps[key], timestamp)
        # If idx is 0, no timestamp is <= the target timestamp
        if index == 0: return ""
        # The element right before the insertion point has the largest timestamp <= targe
        return self.values[key][index - 1]