class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        def subsets(start, combinations):
            output.append(combinations[:])
            for i in range(start, len(nums)):
                # Skip duplicates at the same recursion level
                if i > start and nums[i] == nums[i - 1]:
                    continue
                combinations.append(nums[i])
                subsets(i + 1, combinations)
                combinations.pop()  # Backtrack
        subsets(0, [])
        return output