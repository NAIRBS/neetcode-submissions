# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, level, result):
            if not node: return
            
            # If this is the first node we've visited at this level, 
            # it must be the rightmost one (since we visit right first).
            if level == len(result):
                result.append(node.val)
                
            # Traverse right first, then left
            self.dfs(node.right, level + 1, result)
            self.dfs(node.left, level + 1, result)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.dfs(root, 0, result)
        return result