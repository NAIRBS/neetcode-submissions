class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: return [strs]
        
        final = defaultdict(list)

        result = []
        # Let's make a hashmap to count the char freq for everything I guess
        for i in range(len(strs)):
            hashmap = {}
            for char in strs[i]:
                # looks for char in hashmap, if found return count, if not found return 0
                hashmap[char] = hashmap.get(char, 0) + 1
            # Generate a unique key for each kind of anagram signature (so anagrams will be grouped later)
            key = tuple(sorted(hashmap.items()))
            # Based on the key, add the processed string to the existing value sublist
            final[key].append(strs[i])
        # Only return each value since the keys are not important, only that they are already grouped
        return list(final.values())


                

            


        