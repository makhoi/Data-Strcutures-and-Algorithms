class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return 

            dfs(node.left)
            dfs(node.right)

            if not node.left and node.right:
                res.append(node.right.val)

            if not node.right and node.left:
                res.append(node.left.val)

            return 
        
        dfs(root)
        return res