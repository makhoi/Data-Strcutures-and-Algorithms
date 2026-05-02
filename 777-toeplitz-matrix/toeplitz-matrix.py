class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        def checkDiagonal(rowIndex, colIndex):
            seen = set()
            while rowIndex < ROWS and colIndex < COLS: 
                seen.add(matrix[rowIndex][colIndex])
                if len(seen) > 1:
                    return False

                rowIndex += 1
                colIndex += 1

            return True

        for c in range(COLS):
            if not checkDiagonal(0, c):
                return False

        for r in range(ROWS):
            if not checkDiagonal(r, 0):
                return False
        
        return True