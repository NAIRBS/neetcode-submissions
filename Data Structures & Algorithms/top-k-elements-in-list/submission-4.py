class Solution: # 19th Sep Revision
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # Make a [[], [], []] for each element in nums

        for n in nums:
            count[n] = 1 + count.get(n, 0) # Store count[number] = freq
        for number, count_freq in count.items():
            freq[count_freq].append(number) # group numbers in freq buckets
        res = []
        for i in range(len(freq)-1, 0, -1): # loop backwards through freq buckets
            for n in freq[i]: 
                res.append(n)
                if len(res) == k: # return after hitting kth most frequent!
                    return res