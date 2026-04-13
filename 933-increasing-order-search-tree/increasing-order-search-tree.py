# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        inorder = []

        def dfs(node):
            if not node:
                return 

            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)

            return

        dfs(root)

        dummy = TreeNode(0)
        current = dummy

        for value in inorder:
            current.right = TreeNode(value)
            current = current.right

        return dummy.right