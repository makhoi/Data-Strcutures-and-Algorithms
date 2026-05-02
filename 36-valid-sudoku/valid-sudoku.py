class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLUMNS = len(board[0])

        def checkRow(rowIndex):
            seen = set()
            for c in range(COLUMNS):
                if board[rowIndex][c] == '.':
                    continue
                if board[rowIndex][c] in seen:
                    return False 
                seen.add(board[rowIndex][c])
            return True

        for r in range(ROWS):
            if not checkRow(r):
                return False
        
        def checkColumn(colIndex):
            seen = set()
            for r in range(ROWS):
                if board[r][colIndex] == '.':
                    continue
                if board[r][colIndex] in seen:
                    return False
                seen.add(board[r][colIndex])
            return True
        
        for c in range(COLUMNS):
            if not checkColumn(c):
                return False

        def checkSquare(rowIndex, colIndex):
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
                if not checkSquare(r,c):
                    return False

        return True