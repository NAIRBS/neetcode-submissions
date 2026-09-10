# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def eachlvl(self, root, level, result):
        if not root: return # Base case
        if len(result) <= level: result.append([]) # add a new level/list if not enough
        result[level].append(root.val) # For the specific level, add current node val
        self.eachlvl(root.left, level+1, result) # Run for left subtree
        self.eachlvl(root.right, level+1, result) # Run for right subtree

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self.eachlvl(root, 0, result)
        return result