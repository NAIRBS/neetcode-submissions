class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#===============================================
        # Sort and compare, lamest answer
        # sorted_s = "".join(sorted(s))
        # sorted_t = "".join(sorted(t))

        # if sorted_s == sorted_t: return True
        # else: return False
#===============================================
        return Counter(s) == Counter(t)