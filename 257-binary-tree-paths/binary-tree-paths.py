class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        res = []

        def dfs(node, paths):
            if node.left is None and node.right is None:
                res.append("->".join(paths + [str(node.val)]))

            else:
                paths.append(str(node.val))
                if node.left:
                    dfs(node.left, paths)
                if node.right:
                    dfs(node.right, paths)
                paths.pop()

        dfs(root,[])

        return res
                