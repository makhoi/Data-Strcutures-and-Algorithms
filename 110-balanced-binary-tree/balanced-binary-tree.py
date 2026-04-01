# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [True, 0]

            leftEval = dfs(root.left)
            rightEval = dfs(root.right) 

            balanced = (leftEval[0] and rightEval[0] and abs(leftEval[1] - rightEval[1]) <= 1)

            return [balanced, max(leftEval[1], rightEval[1]) + 1]

        return dfs(root)[0]