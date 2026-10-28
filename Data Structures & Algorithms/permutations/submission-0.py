class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def permutations(candidates, combinations, output):
            if not candidates:
                if combinations not in output:
                    output.append(combinations[:]) # Store a copy only (so pop don't affect)
                return output
            for i in range(len(candidates)):
                combinations.append(candidates[i])
                permutations(candidates[:i] + candidates[i+1:], combinations, output)
                combinations.pop()
        permutations(nums, [], output)
        return output