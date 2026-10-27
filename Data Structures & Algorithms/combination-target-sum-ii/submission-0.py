class Solution: # Technically the same as combination sum 1, note diff below
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = []
        def solve(remaining: int, start: int, combinations: List[int]):
            if remaining == 0:
                output.append(combinations[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue # Added condition to skip dupes at same recursion level
                if candidates[i] > remaining:
                    break # sorted so all after this is too big also!
                combinations.append(candidates[i])
                solve(remaining - candidates[i], i + 1, combinations) # uses i+1 as number can be used only once
                combinations.pop()
        solve(target, 0, [])
        return output