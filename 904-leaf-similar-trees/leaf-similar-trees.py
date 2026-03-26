# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def get_leaves(node): 
            leaves = []

            def dfs(n):
                if not n: 
                    return 
                
                if not n.left and not n.right: 
                    leaves.append(n.val)
                
                dfs(n.left)
                dfs(n.right)

                return 
            
            dfs(node)
            return leaves 
        
        return get_leaves(root1) == get_leaves(root2)

        