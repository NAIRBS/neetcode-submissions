"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node] # Return existing clone if node alr visited
            copy = Node(node.val) # Make a new node with the value if not visited
            oldToNew[node] = copy # Store this in dictionary
            for neighbour in node.neighbors: # For each adjacent node
                copy.neighbors.append(dfs(neighbour)) # Add back each neighbour, either make new or existing clones
            return copy
        return dfs(node)