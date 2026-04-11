class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        if root.val == 0:
            return False

        if root.val == 1:
            return True

        leftEval = self.evaluateTree(root.left)
        rightEval = self.evaluateTree(root.right)

        if root.val == 2:
            return leftEval or rightEval
        
        if root.val == 3:
            return leftEval and rightEval