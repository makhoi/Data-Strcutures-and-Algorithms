# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def dfs(node):
            # current | left | right
            if not node: # node null
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
            return
        '''
        res = [A, B, D, E, C, F, G]
        dfs(A) -> dfs(B) -> dfs(B.left = D) -> dfs(D.left = null)
                                            -> dfs(D.right = null)
                         -> dfs(B.right = E)-> dfs(E.left = null)
                                            -> dfs(E.right = null)
                -> dfs(A.right = C) -> dfs(C.left = F) -> dfs(F.left = null)
                                                       -> dfs(F.right = nul)
                                    -> dfs(C.right = G) -> dfs(G.left = null)
                                                       -> dfs(G.right = nul)
                
        '''

        dfs(root)
        return res