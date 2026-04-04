class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node, total):
            total += node.val

            if node.left is None and node.right is None:
                return total == targetSum

            if node.left:
                result = dfs(node.left, total)
                if result:
                    return True

            if node.right:
                result = dfs(node.right, total)
                if result:
                    return True

            return False

        return dfs(root, 0)