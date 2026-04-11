class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []

        def dfs(node):
            if not node:
                return 
            
            if node.left and not node.right:
                res.append(node.left.val)

            if not node.left and node.right:
                res.append(node.right.val)

            dfs(node.left)
            dfs(node.right)

            return
        
        dfs(root)
        return res