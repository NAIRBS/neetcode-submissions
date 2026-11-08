class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # I can first construct the tree and then find a loop?
        # A tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for neighbour in adj[node]:
                if neighbour == parent:
                    continue
                # If we hit an already visited node that isn't the parent, we found a loop!
                if neighbour in visited:
                    return False
                if not dfs(neighbour, node):
                    return False
            return True

        if not dfs(0, -1): # Start DFS from node 0
            return False
        # Ensure the graph is fully connected (all nodes were reached)
        return len(visited) == n