class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, length, max_freq = 0, 0, 0
        count = {}
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0) # If no key, 1+0, if have key 1+prev_value
            max_freq = max(max_freq, count[s[right]]) # Find the most freq char in the SLIDING WINDOW, NOT s!
            while (right - left + 1) - max_freq > k: # Invalid if window size - max_freq > replacements (k)
                count[s[left]] -= 1 # Reduce count to reevaluate most freq char
                left += 1 # Try to make window size smaller
            length = max(length, right - left + 1)
        return length