class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans = []

        ROWS = len(matrix)
        COLS = len(matrix[0])

        row_total = 0
        for r in range(ROWS):
            for c in range(COLS): 
                row_total += matrix[r][c]
            ans.append(row_total)
            row_total = 0

        return ans