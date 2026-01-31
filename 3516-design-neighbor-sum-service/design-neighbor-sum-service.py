class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        self.grid = grid
        self.position = {}

        for r in range(self.ROWS):
            for c in range(self.COLS):
                self.position[self.grid[r][c]] = (r,c)
        

    def adjacentSum(self, value: int) -> int:
        r,c = self.position[value]

        DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1)]

        sum = 0
        for dr, dc in DIRECTIONS:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < self.ROWS and 0 <= nc < self.COLS:
                sum += self.grid[nr][nc]

        return sum

        

    def diagonalSum(self, value: int) -> int:
        r,c = self.position[value]

        DIRECTIONS = [(-1,-1),(-1,1),(1,-1),(1,1)]

        sum = 0
        for dr, dc in DIRECTIONS:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < self.ROWS and 0 <= nc < self.COLS: 
                sum += self.grid[nr][nc]

        return sum
        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)