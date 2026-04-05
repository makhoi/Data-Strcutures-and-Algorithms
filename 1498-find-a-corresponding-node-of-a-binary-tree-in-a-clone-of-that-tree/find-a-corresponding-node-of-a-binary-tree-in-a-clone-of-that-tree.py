class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(o, c):
            if not o:
                return None

            if o is target:
                return c

            left = dfs(o.left, c.left)
            if left:
                return left

            return dfs(o.right, c.right)

        return dfs(original, cloned)