class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(root1, root2):
            if root1 and root2:
                if root1.val != root2.val:
                    return False
            
            if not root1 and not root2:
                return True
            
            if (root1 and not root2) or (not root1 and root2):
                return False 

            return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)

        return dfs(p,q)