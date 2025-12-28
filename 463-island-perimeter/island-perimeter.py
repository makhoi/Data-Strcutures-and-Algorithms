class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        perimeter = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    perimeter += 4

                    # up
                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 1

                    # down
                    if r < ROWS - 1 and grid[r + 1][c] == 1:
                        perimeter -= 1

                    # left
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 1

                    # right
                    if c < COLS - 1 and grid[r][c+1] == 1: 
                        perimeter -= 1

        return perimeter
