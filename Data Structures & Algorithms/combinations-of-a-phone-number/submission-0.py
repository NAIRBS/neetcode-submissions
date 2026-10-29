class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        output = []
        mappings = {
            1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 
            6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"
        }

        def dfs(index, path):
            if index == len(digits):
                output.append("".join(path))
                return
            for char in mappings[int(digits[index])]:
                path.append(char)
                dfs(index + 1, path)
                path.pop()  # Backtrack

        dfs(0, [])
        return output