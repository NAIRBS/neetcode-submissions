class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Number of edges (in a tree with one extra edge, the number of nodes equals n)
        n = len(edges)
        
        # Initialize an adjacency list for an undirected graph with 1-based indexing (1 to n)
        adj = [[] for _ in range(n+1)] 
        
        # Populate the adjacency list with the given undirected edges
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Keep track of visited nodes during the DFS traversal
        visit = [False] * (n + 1)
        
        # Hash set to store all nodes that belong to the detected cycle
        cycle = set()
        
        # Marker to track where the cycle starts and ends during back-propagation
        cycleStart = -1

        # Recursive Depth First Search (DFS) helper to detect the cycle
        def dfs(node, parent):
            nonlocal cycleStart # Nearest enclosing function scope, for nested (recursive) functions
            
            # 1. Have we been here before?
            if visit[node]:
                cycleStart = node # We found a loop! This node is where the loop starts.
                return True # Break recursive loop
            
            # Mark the current node as visited
            visit[node] = True
            
            # Traverse all neighboring nodes
            for next_index in adj[node]:
                # Skip the direct parent node to prevent immediate backtracking
                if next_index == parent:
                    continue
                
                # Recursively search the neighbor; if a cycle is found along this path...
                if dfs(next_index, node):
                    # As we unwind the recursion, add nodes to the cycle set
                    if cycleStart != -1:
                        cycle.add(node)
                    # Once we have fully traversed back to the cycle's starting node, stop adding
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False

        # Initiate DFS starting from node 1 with no parent (-1)
        dfs(1, -1)

        # Iterate through the original edges in reverse order
        for u, v in reversed(edges):
            # The redundant edge is the last edge in the list where both vertices lie inside the cycle
            if u in cycle and v in cycle:
                return [u, v]
                
        return [] # If no edge found that results in a cycle...