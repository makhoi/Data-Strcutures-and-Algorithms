class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        def setRow(r):
            for c in range(COLS):
                if matrix[r][c] != 0:
                    matrix[r][c] = float('inf')
        
        def setColumn(c):
            for r in range(ROWS):
                if matrix[r][c] != 0:
                    matrix[r][c] = float('inf')

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    setRow(r)
                    setColumn(c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == float('inf'):
                    matrix[r][c] = 0

        