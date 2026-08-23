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
        # Time: o(n+m), n,m = size of both str, added as it goes through both iteratively
        # Space: o(1), as at most 26 different char (hash map is counting occurance of each char)

        # if len(s) != len(t): 
        #     return False

        # countS, countT = {}, {}
        # for i in range(len(s)):
        #     # dictionary.get(key, def_val), key: name of key to look up, def_val: returns if key missing
        #     countS[s[i]] = 1 + countS.get(s[i], 0) # This adds 1 to the existing count of each char in the hashmap
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        # return countS == countT
#===============================================
        # Using Hash Table (using fixed 26 len array to count chars)
        # Time: o(n+m), same reason as above
        # Space: Still o(1) as only 26 char.

        if len(s) != len(t):
            return False
        counter = [0] * 26
        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1 #In list, convert value of string to 1-26, add 1 if char in str s
            counter[ord(t[i]) - ord('a')] -= 1 #In list, convert value of string to 1-26, add 1 if char in str t
        for count in counter:
            if count != 0:
                return False
        return True

        

