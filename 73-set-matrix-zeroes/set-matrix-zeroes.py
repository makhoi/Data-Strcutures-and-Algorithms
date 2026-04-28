class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])

        def setRow(rowIndex):
            for c in range(COLS):
                if matrix[rowIndex][c] != 0:
                    matrix[rowIndex][c] = float('inf')
        
        def setColumn(colIndex):
            for r in range(ROWS):
                if matrix[r][colIndex] != 0:
                    matrix[r][colIndex] = float('inf')
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    setRow(r)
                    setColumn(c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == float('inf'):
                    matrix[r][c] = 0