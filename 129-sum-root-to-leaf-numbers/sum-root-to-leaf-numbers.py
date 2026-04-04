class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        total = 0

        def dfs(node, currentPath):
            nonlocal total

            if node.left is None and node.right is None:
                total += int("".join(currentPath + [str(node.val)]))
            else:
                currentPath.append(str(node.val))
                if node.left:
                    dfs(node.left, currentPath)
                if node.right:
                    dfs(node.right, currentPath)
                currentPath.pop()

        dfs(root, [])
        return total