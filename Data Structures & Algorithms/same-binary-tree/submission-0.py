# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True # If both don't have node = equal = True
        if not p or not q or p.val != q.val: return False # If one side missing node or unequal val = False
        left = self.isSameTree(p.left, q.left) # Check left subtree
        right = self.isSameTree(p.right, q.right) # Check right subtree
        return left and right # At the end combine it all, it should eventually reach no nodes = True!