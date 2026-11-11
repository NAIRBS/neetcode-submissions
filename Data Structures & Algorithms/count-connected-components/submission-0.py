class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node):
            q = deque([node])
            visit[node] = True
            while q:
                curr = q.popleft()
                for next_index in adj[curr]:
                    if not visit[next_index]:
                        visit[next_index] = True
                        q.append(next_index)
        result = 0
        for node in range(n):
            if not visit[node]:
                bfs(node)
                result += 1 # This is actually pretty similar to connected islands...?
        return result