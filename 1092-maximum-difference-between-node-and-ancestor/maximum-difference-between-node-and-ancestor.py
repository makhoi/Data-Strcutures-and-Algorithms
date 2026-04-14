class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr_min, curr_max):
            if not node:
                return curr_max - curr_min
            
            curr_min = min(curr_min, node.val)
            curr_max = max(curr_max, node.val)

            left_max_diff = dfs(node.left, curr_min, curr_max)
            right_max_diff = dfs(node.right, curr_min, curr_max)

            return max(left_max_diff, right_max_diff)
        
        return dfs(root, root.val, root.val)