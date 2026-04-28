class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Iterate over every elements in the matrix
        -> determine the coordinates of all the element which value is 0
        lets say it is [a,b] -> convert every element in that row (if not 0 to .)
        have a list to store coordinations of all the 0s
        then comeback and convert all the . into 0
        """

        ROWS = len(matrix)
        COLS = len(matrix[0])

        zeros = []

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zeros.append([r,c])
        
        for r,c in zeros:
            for col in range(COLS):
                if matrix[r][col] != 0 and matrix[r][col] != float('inf'):
                    matrix[r][col] = float('inf')

            for row in range(ROWS):
                if matrix[row][c] != 0 and matrix[row][c] != float('inf'):
                    matrix[row][c] = float('inf')

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == float('inf'):
                    matrix[r][c] = 0

