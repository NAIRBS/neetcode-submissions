class Solution: # 17th Sep 2026 Revisit
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        hashmap_s, hashmap_t = {}, {}
        for i in range(len(s)): 
            if s[i] not in hashmap_s: hashmap_s[s[i]] = 1
            else: hashmap_s[s[i]] += 1
            if t[i] not in hashmap_t: hashmap_t[t[i]] = 1
            else: hashmap_t[t[i]] += 1
        return hashmap_s == hashmap_t