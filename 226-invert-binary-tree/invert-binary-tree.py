class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        leftEval = self.invertTree(root.left)
        rightEval = self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root