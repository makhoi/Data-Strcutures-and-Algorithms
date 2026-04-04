class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(node):
            if not node:
                return 
            
            if node.left and node.left.left is None and node.left.right is None:
                res.append(node.left.val)
            
            dfs(node.left)
            dfs(node.right)

            return 
        
        dfs(root)

        return sum(res)