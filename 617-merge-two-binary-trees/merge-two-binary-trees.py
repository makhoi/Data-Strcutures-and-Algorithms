class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        
        if root1 is None and root2:
            return root2
        
        if root1 and root2 is None:
            return root1

        if root1 and root2:
            root1.val = root1.val + root2.val

        root1.left = self.mergeTrees(root1.left if root1.left else None, root2.left if root2.left else None)
        root1.right = self.mergeTrees(root1.right if root1.right else None,root2.right if root2.right else None)

        return root1
