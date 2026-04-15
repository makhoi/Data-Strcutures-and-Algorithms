class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        '''
        Deepest leaf = leaf at highest level
        how to determine it is a highest level? 
        '''

        def maxHeight(node):
            if not node:
                return 0

            leftEval = maxHeight(node.left)
            rightEval = maxHeight(node.right)

            return 1 + max(leftEval, rightEval)

        deepest_level = maxHeight(root) - 1

        deepest_leaves = []
        def deepestLeaves(node, level):
            if not node:
                return

            if level == deepest_level:
                deepest_leaves.append(node.val)

            deepestLeaves(node.left, level + 1)
            deepestLeaves(node.right, level + 1)
                
        deepestLeaves(root, 0)
                
        return sum(deepest_leaves)