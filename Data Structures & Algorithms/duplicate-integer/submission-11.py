class Solution: # Recap 17th Sep 2026
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in range(len(nums)):
                if nums[i] in hashmap: return True
                else: hashmap[nums[i]] = 1
        return False