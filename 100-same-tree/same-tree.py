class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(node, res):
            if not node:
                res.append(None)
            else:
                res.append(node.val)
                dfs(node.left, res)
                dfs(node.right, res)

            return 

        res1 = []
        dfs(p, res1)

        res2 = []
        dfs(q, res2)

        return res1 == res2