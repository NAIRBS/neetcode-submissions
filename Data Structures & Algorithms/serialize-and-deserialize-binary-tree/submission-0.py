# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(root, result):
            if not root:
                result.append(None)
                return
            result.append(root.val)        # Visit root
            dfs(root.left, result)  # Visit left subtree
            dfs(root.right, result) # Visit right subtree
        res_list = []
        dfs(root, res_list)
        return str(res_list)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Safely convert the string representation of a list back into a real Python list
        # Using iterator (via iter() or popping from an index) prevents slow O(N) list pops
        nodes_list = ast.literal_eval(data)
        nodes_iter = iter(nodes_list)
        def deserialize_preorder():
            try:
                val = next(nodes_iter)
            except StopIteration:
                return None
            if val is None:
                return None
            root = TreeNode(val)
            root.left = deserialize_preorder()
            root.right = deserialize_preorder()
            return root
        return deserialize_preorder()