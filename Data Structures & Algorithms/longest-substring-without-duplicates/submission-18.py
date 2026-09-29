class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, longest = 0, 1, 0
        substring = set()
        for right in range(len(s)):
            while s[right] in substring:
                substring.remove(s[left])
                left += 1
            substring.add(s[right])
            longest = max(longest, right - left + 1)
            right += 1
        return longest