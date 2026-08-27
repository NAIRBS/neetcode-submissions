class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) : return ""
        freq1 = {}
        freq2 = {} # Freq count of t
        for char in t: # Store freq of t
            freq2[char] = 1 + freq2.get(char, 0)
        left = 0
        min_len = float('inf')
        output = ""
        formed = 0
        required = len(freq2) # Total unique characters needed from t
        for right in range(len(s)):
            freq1[s[right]] = freq1.get(s[right], 0) + 1 # Store freq of s
            # If the frequency of the current char matches its needed count in t, increment formed
            if s[right] in freq2 and freq1[s[right]] == freq2[s[right]]: 
                formed += 1
            while left <= right and formed == required:
                # Update output if we found a smaller valid window
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    output = s[left:right+1]
                # Shrink window from the left
                left_char = s[left]
                freq1[left_char] -= 1
                # If dropping this character breaks the required count, decrement formed
                if left_char in freq2 and freq1[left_char] < freq2[left_char]: 
                    formed -= 1
                left += 1
        return output