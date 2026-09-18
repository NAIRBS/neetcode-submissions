class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashmap: return [min(i, hashmap[difference]), max(hashmap[difference], i)]
            hashmap[nums[i]] = i
        return False