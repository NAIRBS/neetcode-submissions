# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None # If no root
        tmp = root.left # Swap children of the root
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left) # Do again on all the stuff on left
        self.invertTree(root.right) # Do again on all stuff on right
        return root