class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(node):
            if not node:
                return

            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

            return
        
        dfs(root)

        return len(res)