class Solution: # 24th Sep Revision
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_hashset = set(nums)
        longest_count = 0
        for num in nums_hashset:
            if (num - 1) not in nums_hashset: # Find the start of sequence
                length = 1
                while (num + length) in nums_hashset:
                    length += 1
                longest_count = max(length, longest_count)
        return longest_count
