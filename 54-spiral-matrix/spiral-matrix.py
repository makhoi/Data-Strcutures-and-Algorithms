class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        result = []
        while left <= right and top <= bottom:
            
            # top row: 
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1

            # right edge
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1

            # bottom row
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1

            # left edge
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1

        return result