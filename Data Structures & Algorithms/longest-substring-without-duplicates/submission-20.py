class Solution: # 1st Oct Revision AGAIN
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, length, substring = 0, 0, 0, set()
        while right < len(s): # While window in search space
            while s[right] in substring: # If right wall char in substring, make the window smaller on left
                substring.remove(s[left])
                left += 1
            substring.add(s[right]) # Move window to the right
            length = max(length, len(substring)) # Find current length
            right += 1 # Move pointer right
        return length