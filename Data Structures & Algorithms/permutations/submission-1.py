class Solution: # Clean up solution
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def permutations(candidates, combinations):
            if not candidates:
                output.append(combinations[:]) # Store a copy only (so pop don't affect)
                return output
            for i in range(len(candidates)):
                combinations.append(candidates[i])
                permutations(candidates[:i] + candidates[i+1:], combinations)
                combinations.pop()
        permutations(nums, [])
        return output