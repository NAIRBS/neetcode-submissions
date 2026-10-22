class Solution: # 22nd Oct 2026 Revision
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast, slow2 = nums[0], nums[nums[0]], 0 # Treat it as linked list...
        while slow != fast: # Find the point where they meet
            slow = nums[slow]
            fast = nums[nums[fast]]
        while slow != slow2: # After that interate until repeated integer is found!
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow