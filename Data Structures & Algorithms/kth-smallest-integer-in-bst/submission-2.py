# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        while curr:
            if not curr.left: # If no left subtree, current is now the next smallest.
                k -= 1
                if k == 0: return curr.val
                curr = curr.right # Move to right subtree
            else:
                # Find the in-order predecessor (the rightmost node in the left subtree).
                pred = curr.left # Have left subtree so move there
                while pred.right and pred.right != curr: # if predecessor have 
                    pred = pred.right # Move right
                # If the predecessor's right pointer is empty, we haven't visited 
                # the left subtree yet. Create a temporary "thread" back to curr.
                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                # If thread existes, left subtree is finished
                else:
                    pred.right = None
                    k -= 1
                    if k == 0: return curr.val
                    curr = curr.right
        return -1