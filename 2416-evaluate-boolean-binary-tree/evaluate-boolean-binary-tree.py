# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        '''
        0. Define function: 
        - input: root
        - output: T/F 
        -> leftEval, rightEval: 
        '''
        if root.val == 1:
            return True
        if root.val == 0:
            return False 
        
        leftEval = self.evaluateTree(root.left)
        rightEval = self.evaluateTree(root.right)

        if root.val == 2: 
            return leftEval or rightEval

        if root.val == 3: 
            return leftEval and rightEval
        
        # return True 