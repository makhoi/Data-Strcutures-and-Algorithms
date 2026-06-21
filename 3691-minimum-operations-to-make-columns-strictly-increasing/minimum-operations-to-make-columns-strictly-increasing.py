class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        COLS = len(grid[0])
        ROWS = len(grid)

        count = 0
        for c in range(COLS):
            for r in range(1, ROWS):
                if grid[r][c] > grid[r-1][c]:
                    continue
                else:
                    count += grid[r-1][c] + 1 - grid[r][c]
                    grid[r][c] = grid[r-1][c] + 1
                
        return count