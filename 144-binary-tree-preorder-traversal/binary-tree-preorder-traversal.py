class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []

        def dfs(node):
            if not node: 
                return
            
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

            return 
        
        dfs(root)

        return res