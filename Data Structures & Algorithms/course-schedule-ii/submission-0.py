class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Initialize the adjacency list and in-degree array
        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        
        # Populate graph and compute in-degrees
        for nxt, pre in prerequisites:
            indegree[nxt] += 1       # 'nxt' course depends on 'pre', so increase its in-degree count
            adj[pre].append(nxt)     # Add 'nxt' to the adjacency list of 'pre'

        output = []

        # Step 2: Define a recursive helper function (similar to Kahn's Algorithm using recursion)
        def dfs(node):
            output.append(node)      # Add the current course to the final topological order
            indegree[node] -= 1      # Decrement in-degree to mark this node as processed (becomes -1)
            
            # Visit all neighboring courses (courses that depend on the current course)
            for nei in adj[node]:
                indegree[nei] -= 1   # One prerequisite has been satisfied, so decrease its in-degree
                
                # If all prerequisites for the neighbor are now met (in-degree is 0), process it recursively
                if indegree[nei] == 0:
                    dfs(nei)

        # Step 3: Kick off the traversal for all courses that initially have 0 prerequisites
        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)

        # Step 4: Verify if all courses were ordered (checks for cycles). 
        # If a cycle exists, some nodes will never reach an in-degree of 0.
        return output if len(output) == numCourses else []