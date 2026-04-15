class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
        
        if original is target:
            return cloned

        leftEval = self.getTargetCopy(original.left, cloned.left, target)
        rightEval = self.getTargetCopy(original.right, cloned.right, target)

        if leftEval:
            return leftEval
        else:
            return rightEval