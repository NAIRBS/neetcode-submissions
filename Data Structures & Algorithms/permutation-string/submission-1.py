class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        freq1 = {} # Freq count of S1
        freq2 = {} # Freq count of S2
        for char in s1: # Store freq of S1
            freq1[char] = 1 + freq1.get(char, 0)
        left = 0
        for right in range(len(s2)): # Look for every window of same size of s1
            while right - left + 1 > len(s1): # Shrink window when too BIG
                freq2[s2[left]] -= 1 # Reduce freq count since shrinking
                if freq2[s2[left]] == 0: del freq2[s2[left]] # If reach zero, remove entry
                left += 1 # Sliding window
            freq2[s2[right]] = freq2.get(s2[right], 0) + 1 # Store freq of S2
            if freq1 == freq2: return True
        return False
        
        