class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, longest_length, max_freq = 0, 0, 0
        count = {}
        for right in range(len(s)):
            # Track frequency of the current character
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
            # If characters to replace exceed k, shrink the window from the left
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            longest_length = max(longest_length, right - left + 1)
        return longest_length