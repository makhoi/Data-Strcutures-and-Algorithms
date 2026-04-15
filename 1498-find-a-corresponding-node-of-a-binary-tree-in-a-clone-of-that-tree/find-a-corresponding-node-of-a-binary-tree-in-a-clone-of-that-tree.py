class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def dfs(node1, node2):
            if not node1:
                return None
            
            if node1 is target:
                return node2

            leftEval = dfs(node1.left, node2.left)
            rightEval = dfs(node1.right, node2.right)

            if leftEval:
                return leftEval
            else:
                return rightEval

        return dfs(original, cloned)