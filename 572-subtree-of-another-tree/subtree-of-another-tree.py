class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # perform postorder traversal on both tree first
        def dfs(node, arr):
            if not node:
                arr.append(None)
            else:
                dfs(node.left, arr)
                dfs(node.right, arr)
                arr.append(node.val)

            return
        
        arr1 = []
        dfs(root, arr1)

        arr2 = []
        dfs(subRoot, arr2)

        # find if there is subRoot in original tree
        n = len(arr1)
        m = len(arr2)

        for i in range(n-m+1):
            if arr1[i:i+m] == arr2:
                return True
        
        return False