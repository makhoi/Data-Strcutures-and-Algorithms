class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        leftEval = self.isSameTree(p.left, q.left)
        rightEval = self.isSameTree(p.right, q.right)

        return leftEval and rightEval
        