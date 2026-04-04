class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
            
        def dfs(node, total):
            total += node.val

            if node.left is None and node.right is None:
                return total == targetSum

            if node.left and dfs(node.left, total):
                return True

            if node.right and dfs(node.right, total):
                return True

            return False

        return dfs(root, 0)