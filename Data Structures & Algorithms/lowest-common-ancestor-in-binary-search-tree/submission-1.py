# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # We definitely need to abuse the fact that this is a BINARY search tree
        current = root
        while current:
            # If both p and q are greater than current, LCA must be in the right subtree
            if p.val > current.val and q.val > current.val:
                current = current.right
            # If both p and q are smaller than current, LCA must be in the left subtree
            elif p.val < current.val and q.val < current.val:
                current = current.left
            # We found the split point (or one of the nodes is the ancestor of the other)
            else:
                return current