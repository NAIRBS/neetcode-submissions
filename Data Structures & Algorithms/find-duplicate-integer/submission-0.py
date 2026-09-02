class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else: return num