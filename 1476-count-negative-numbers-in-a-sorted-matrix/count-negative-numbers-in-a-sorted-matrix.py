class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        COLS = len(grid[0])
        ROWS = len(grid)

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] < 0:
                    count += 1

        return count