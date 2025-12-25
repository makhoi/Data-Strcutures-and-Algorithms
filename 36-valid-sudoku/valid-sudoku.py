class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(r):
            seen = set()
            arr = board[r]
            for val in arr:
                if val == '.':
                    continue
                if val in seen:
                    return False
                seen.add(val)
            return True
        
        for r in range(9):
            if not checkRow(r):
                return False

        def checkCol(c):
            seen = set()
            for r in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                if val in seen:
                    return False
                seen.add(val)
            return True

        for c in range(9):
            if not checkCol(c):
                return False

        def checkBoard(rowIdx, colIdx):
            seen = set()
            for r in range(rowIdx, rowIdx + 3):
                for c in range(colIdx, colIdx + 3): 
                    val = board[r][c]
                    if val == '.':
                        continue
                    if val in seen:
                        return False
                    seen.add(val)
            return True

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                if not checkBoard(r,c):
                    return False
        return True
        