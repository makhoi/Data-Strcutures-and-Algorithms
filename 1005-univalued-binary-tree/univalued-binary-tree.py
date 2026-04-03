class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root is None: 
            return True
        
        leftEval = self.isUnivalTree(root.left)
        rightEval = self.isUnivalTree(root.right)
        
        if root.left and root.val != root.left.val:
            return False

        if root.right and root.val != root.right.val:
            return False

        return leftEval and rightEval