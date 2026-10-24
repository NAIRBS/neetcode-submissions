class Solution: # Cleaned up
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []
        def solve(remaining: int, start: int, combinations: List[int]):
            if remaining == 0:
                output.append(combinations[:])
                return
            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    break # sorted so all after this is too big also!
                combinations.append(nums[i])
                solve(remaining - nums[i], i, combinations) # i, not i + i, so num can be reused
                combinations.pop()
        solve(target, 0, [])
        return output