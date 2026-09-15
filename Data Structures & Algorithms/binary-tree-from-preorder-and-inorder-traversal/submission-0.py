# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Preorder: Root -> Left -> Right -> Next Layer
# Inorder:  Left -> Root -> Right -> Next Layer

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode(None)
        curr = head
        pre_index, inorder_index, n = 0, 0, len(preorder) 
        while pre_index < n and inorder_index < n: # Go right then as far left as possible
            curr.right =  TreeNode(preorder[pre_index], right = curr.right)
            curr = curr.right
            pre_index += 1
            while pre_index < n and curr.val != inorder[inorder_index]: # Build left subtrees
                curr.left = TreeNode(preorder[pre_index], right = curr)
                curr = curr.left
                pre_index += 1
            inorder_index += 1 # Advance inorder index
            # Backtracking phase
            while curr.right and inorder_index < n and curr.right.val == inorder[inorder_index]:
                prev = curr.right
                curr.right = None
                curr = prev
                inorder_index += 1
        return head.right
