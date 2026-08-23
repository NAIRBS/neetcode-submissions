class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#===============================================
        # Sort and compare, lamest answer
        # sorted_s = "".join(sorted(s))
        # sorted_t = "".join(sorted(t))

        # if sorted_s == sorted_t: return True
        # else: return False

        # more concise solution is:
        # return sorted(s) == sorted(t
#===============================================
        # Just add the char ascii values of each string, honestly the most "clever" solution.
        # return Counter(s) == Counter(t)
#===============================================
        # Using Hash Maps, 
        # time: o(n+m), n,m = size of both str, added as it goes through both iteratively
        # space: o(1), as at most 26 different char (hash map is counting occurance of each char)

        if len(s) != len(t): 
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            # dictionary.get(key, def_val), key: name of key to look up, def_val: returns if key missing
            countS[s[i]] = 1 + countS.get(s[i], 0) # This adds 1 to the existing count of each char in the hashmap
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
#===============================================
        #if len(s) != len(t):

