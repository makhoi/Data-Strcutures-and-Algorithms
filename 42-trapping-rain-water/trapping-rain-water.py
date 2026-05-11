class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        at index i, find max left and max right
        count water trapped = min(maxLeft, maxRight) - height[i]
        '''
        n = len(height)

        max_lefts = [0]*n
        max_left = 0
        for i in range(n):
            max_lefts[i] = max_left
            if height[i] > max_left:
                max_left = height[i]

        max_rights = [0]*n
        max_right = 0
        for i in range(n - 1, -1, -1):
            max_rights[i] = max_right
            if height[i] > max_right:
                max_right = height[i]

        res = 0
        trap = 0
        for i in range(n):
            trap = min(max_lefts[i], max_rights[i]) - height[i]
            res += trap if trap > 0 else 0
            trap = 0

        return res