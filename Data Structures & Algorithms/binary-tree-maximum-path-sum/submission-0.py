# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val] # can change things inside list but not int
        def dfs(root):
            if not root: return 0 # Base case
            leftMax = dfs(root.left) # max sum on left
            rightMax = dfs(root.right) # max sum on right
            leftMax = max(leftMax, 0) # if negative, force it to be 0
            rightMax = max(rightMax, 0) # same as above
            result[0] = max(result[0], root.val + leftMax + rightMax) # find the maximum at anytime
            return root.val + max(leftMax, rightMax) # return the max at the end
        dfs(root)
        return result[0]