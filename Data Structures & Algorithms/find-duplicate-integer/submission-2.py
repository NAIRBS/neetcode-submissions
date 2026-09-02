class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Stupid poopoo head solution :(, used o(n) space
        # hashmap = {}
        # for num in nums:
        #     if num not in hashmap:
        #         hashmap[num] = 1
        #     else: return num
        # Also we can't sort it since it would modify the nums array

        # If we look at index based: [0, 1, 2, 3, 4, 5]
        #   but the actual value is: [1, 2, 3, 4, 5, 5]
        # We can assume that the VALUE is the "next" node/index to point towards!
        # Even if its out of ascending order, each node should naturally point towards each other
        # Since it will all point to each other until the "linked list" runs completely
        # We can also see that if there is a repeating value, it will end up as a loop
        # So all we gotta do is use tortoise and hare algo to detect the element causing the loop back.
        slow, fast, slow2 = nums[0], nums[nums[0]], 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow