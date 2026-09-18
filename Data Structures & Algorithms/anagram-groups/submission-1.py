class Solution: # 18th Sep 2026 Revision
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_maps = []
        result =  defaultdict(list)
        for i, str_item in enumerate(strs):
            freq_map = {}
            for char in str_item:
                if char in freq_map: freq_map[char] += 1
                else: freq_map[char] = 1
            key = tuple(sorted(freq_map.items()))
            result[key].append(strs[i])
        return list(result.values())