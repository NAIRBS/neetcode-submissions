class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        def solve(remaining: int, combinations: List[int], candidates: List[int], output: List[List[int]]):
            if remaining == 0:
                output.append(combinations[:])
                return
            elif remaining < 0:
                return
            for index, num in enumerate(candidates):
                combinations.append(num)
                solve(remaining-num, combinations, candidates[index:], output)
                combinations.pop()
        solve(target, [], nums, output)
        return output