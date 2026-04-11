class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []

        def dfs(node):
            if not node:
                return # return to previous call

            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

            return 

        dfs(root)

        return res