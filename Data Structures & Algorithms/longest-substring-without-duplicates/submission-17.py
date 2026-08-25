class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) <= 1: return len(s)
        # if len(s) == 2:
        #     if s[0] != s[1]: return 2
        #     else: return 1
        # left, right = 0, 1
        # length = 1
        # seen = {s[left]: left} # Store index in hashmap
        # while right < len(s):
        #     if s[right] in seen: # If duplicate found
        #         left = max(left, seen[s[right]] + 1)
        #     seen[s[right]] = right
        #     length = max(length, (right - left) + 1)
        #     right += 1
        # return length

        # Model Answer
        seen = {}
        left = 0
        length = 0

        for right in range(len(s)):
            if s[right] in seen:
                left = max(seen[s[right]] + 1, left)
            seen[s[right]] = right
            length = max(length, right - left + 1)
        return length