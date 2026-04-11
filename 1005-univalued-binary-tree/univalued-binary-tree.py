class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        res = set()

        def dfs(node):
            if not node:
                return 
            
            res.add(node.val)
            dfs(node.left)
            dfs(node.right)

            return

        dfs(root)
        return len(res) == 1