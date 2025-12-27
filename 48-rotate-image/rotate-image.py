class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Transpose 
        t = [[0]*n for _ in range(n)]

        for r in range(n):
            for c in range(n):
                t[r][c] = matrix[c][r]

        # Rotate
        for r in range(n):
            left = 0
            right = n - 1
            while left < right:
                t[r][left], t[r][right] = t[r][right], t[r][left]
                left += 1
                right -= 1

        for r in range(n):
            matrix[r] = t[r]
        
        