class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s, hashmap_t = {}, {}
        for i in range(len(s)): 
            if s[i] not in hashmap_s: hashmap_s[s[i]] = 1
            else: hashmap_s[s[i]] += 1
        for i in range(len(t)): 
            if t[i] not in hashmap_t: hashmap_t[t[i]] = 1
            else: hashmap_t[t[i]] += 1
        return hashmap_s == hashmap_t