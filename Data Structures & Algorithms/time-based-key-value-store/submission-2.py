class TimeMap:

    def __init__(self):
        self.hashmap = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        # For a given key, look at all the times set was called in the past and check their recorded timestamps.
        # Only care about timestamps that happened at/before target timestamp 
        # (timestamp_prev <= timestamp). Ignore any future timestamps.
        # If you find multiple valid timestamps, choose the largest number among the valid ones.
        # If the key doesn't exist, or key happened after your target timestamp, return an empty string "".
        if key not in self.hashmap: return ""
        most_recent = -1
        output = "" # If cannot find a timestamp, default to ""
        # Naive for loop goes to o(n)
        # for val, time in self.hashmap[key]:
        #     if time > timestamp: continue
        #     if time > most_recent:
        #         most_recent = time
        #         output = val

        # I guess its binary search time for o(logn)
        # All the timestamps of set are strictly increasing. << Means its sorted in ascending order!!!
        left, right = 0, len(self.hashmap[key])-1
        while left <= right:
            middle = (left + right) // 2
            if self.hashmap[key][middle][1] == timestamp: return self.hashmap[key][middle][0]
            if self.hashmap[key][middle][1] > timestamp: # Timestamp found bigger, abandon right, search left
                right = middle - 1
            elif self.hashmap[key][middle][1] < timestamp: # Timestamp found smaller, abandon left, search right
                left = middle + 1
                output =  self.hashmap[key][middle][0] 
        return output
