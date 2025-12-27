class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose 
        ROWS = COLS = len(matrix) 

        transpose_matrix = [[0]*ROWS for _ in range(COLS)]

        for r in range(ROWS):
            for c in range(COLS): 
                transpose_matrix[c][r] = matrix[r][c]
        
        # Rotate
        for r in range(ROWS):
            left = 0
            right = COLS - 1

            while left < right: 
                transpose_matrix[r][left], transpose_matrix[r][right] = transpose_matrix[r][right], transpose_matrix[r][left]
                left += 1
                right -= 1

        for r in range(ROWS):
            matrix[r] = transpose_matrix[r]
        