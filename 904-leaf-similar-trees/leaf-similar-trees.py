class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node, res):
            if not node:
                return
            
            if not node.left and not node.right:
                res.append(node.val)

            dfs(node.left, res)
            dfs(node.right, res)

            return
        
        res1 = []
        dfs(root1, res1)

        res2 = []
        dfs(root2, res2)

        return res1 == res2