# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False # If main tree empty but subroot exist, is invalid
        if not subRoot: return True # If subRoot is empty/None, consider valid subtree
        if root.val != subRoot.val: # If current node in main is not a match, move on to left and right nodes
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
            return left or right
        else: # If values match in the main and sub tree, find if from that starting node if its identical
            def is_identical(root, subRoot):
                if not root and not subRoot: return True # Traversed both trees completely so True
                if not root or not subRoot or root.val != subRoot.val: return False # Didn't end tgt or != Val
                left = is_identical(root.left, subRoot.left) # Compare whole of left subtree
                right = is_identical(root.right, subRoot.right) # Compare whole of right subtree
                return left and right # Return if both left and right subtrees says equal
            if is_identical(root, subRoot): return True # If found subtree, directly return True
        left = self.isSubtree(root.left, subRoot) # If val matches at the start (but fail to find match), continue
        right = self.isSubtree(root.right, subRoot) # Same for right subtree
        return left or right