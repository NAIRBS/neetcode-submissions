class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Worse kind of solution
        # count = 0
        # for i in nums:
        #     for j in nums:
        #         if i == j:
        #             count+=1
        #     if count > 1:
        #         return True
        #     count = 0
        # return False

        # Slightly better version
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue  # Skip comparing the element to itself
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # Hashmap?? << Too slow
        # seen = {}
        # for i in range(len(nums)):
        #     if nums[i] in seen.values():
        #         return True
        #     seen[i] = nums[i]
        # return False

        # Hashmap << Faster?? (It works but it is space inefficient...)
        # seen = {}
        # for i in range(len(nums)):
        #     if nums[i] in seen:
        #         return True
        #     seen[nums[i]] = nums[i]
        # return False

        # lets use a hash set instead?
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False         


