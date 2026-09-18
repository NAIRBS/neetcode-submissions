class Solution: # 18th Sep 2026 Revision
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result =  defaultdict(list) #auto create default val with missing key ref
        for i, str_item in enumerate(strs):
            freq_map = {}
            for char in str_item:
                if char in freq_map: freq_map[char] += 1
                else: freq_map[char] = 1
            key = tuple(sorted(freq_map.items()))
            result[key].append(strs[i]) # Make a list of words
        return list(result.values())