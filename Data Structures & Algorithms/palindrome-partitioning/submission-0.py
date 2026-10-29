class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(i, path):
            if i == len(s):
                res.append(path)
                return
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if sub == sub[::-1]: # If the current substring is a palindrome, explore further
                    dfs(j + 1, path + [sub])
        dfs(0, [])
        return res