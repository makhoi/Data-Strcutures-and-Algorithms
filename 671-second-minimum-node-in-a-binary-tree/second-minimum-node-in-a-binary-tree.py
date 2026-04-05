class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        res = None

        def dfs(node):
            nonlocal res

            if not node:
                return

            if node.val > root.val:
                if res is None or node.val < res:
                    res = node.val

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return res if res != None else -1