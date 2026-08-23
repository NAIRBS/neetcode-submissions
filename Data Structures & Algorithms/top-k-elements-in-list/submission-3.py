class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # numcount = {}
        # # Store data in number:count hashmap
        # for num in nums:
        #     if num in numcount:
        #         numcount[num] += 1
        #     else:
        #         numcount[num] = 1

        # # Make another hashmap that flips the key:value to become count:number
        # # Sort the map by the count in descending order, filter out the bottom (highest) counts of numbers
        # sorted_map = (sorted(numcount.items(), key=lambda item: item[1], reverse=True)[:k])

        # # Return list of numbers
        # return [item[0] for item in sorted_map]

        # Model Answer
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # Make a [[], [], []] for each element in nums
        # We do this JUST in case there is unique number for every number in nums...

        for n in nums:
            count[n] = 1 + count.get(n, 0) # Quick one liner that lets you store count[number] = freq, 
            # ,0 is default value returned if cannot return value of the key.
        for n, c in count.items(): # .items() returns a tuple of all elements in the dict/hashmap
            freq[c].append(n) # For each unique number and freq in count, store the data format freq[freq] = number
            # We append as we can store MULTIPLE numbers in the list for the same freq count!
            # Eg. freq[2] = [5,6] << Both 5 and 6 showed up 2 times each
        
        res = []
        for i in range(len(freq)-1, 0, -1): # for each element in freq, go in reverse (because higher freq at end)
            for n in freq[i]: # For each thingy in each list
                res.append(n) # Append it to res (result)
                if len(res) == k: # Once there is at least k number found, immediately return
                    return res



        
        
