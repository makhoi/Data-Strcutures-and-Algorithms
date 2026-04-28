class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ROWS = len(board)
        COLS = len(board[0])

        def isValidRow(rowIndex):
            seen = set()
            for c in range(COLS):
                if board[rowIndex][c] == '.':
                    continue
                if board[rowIndex][c] in seen:
                    return False
                seen.add(board[rowIndex][c])
            return True
        
        for row in range(ROWS):
            if not isValidRow(row):
                return False

        def isValidColumn(colIndex):
            seen = set()
            for r in range(ROWS):
                if board[r][colIndex] == '.':
                    continue
                if board[r][colIndex] in seen:
                    return False
                seen.add(board[r][colIndex])
            return True
        
        for col in range(COLS):
            if not isValidColumn(col):
                return False

        def isValidSquare(rowIndex, colIndex): 
            seen = set()
            for r in range(rowIndex, rowIndex + 3):
                for c in range(colIndex, colIndex + 3):
                    if board[r][c] == '.':
                        continue
                    if board[r][c] in seen:
                        return False
                    seen.add(board[r][c])
            return True
        
        for r in range(0,9,3):
            for c in range(0,9,3):
                if not isValidSquare(r,c):
                    return False

        return True