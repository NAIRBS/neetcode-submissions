class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Cringe o(n^2) solution:

        # for i in range(len(nums)):
        #     remainder = target - nums[i]
        #     for j in range(len(nums)):
        #         if i == j: continue
        #         if nums[j] == remainder:
        #             if i > j: return [j,i]
        #             else: return [i,j]
        
        # Hash Map time...again.
        hashmap = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in hashmap:
                return [hashmap[remainder], i] # i will always be larger as remainder is alr stored
            hashmap[nums[i]] = i # Store the value already compared as another remainder to be found
