class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numcount = {}
        countnum = {}
        keys = []

        output = []  
        values = []
        # Store data in number:count hashmap
        for num in nums:
            if num in numcount:
                numcount[num] += 1
            else:
                numcount[num] = 1
                keys.append(num) # Note the new key (number) found
        sorted_map = (sorted(numcount.items(), key=lambda item: item[1], reverse=True)[:k])
        return [item[0] for item in sorted_map]



        
        
