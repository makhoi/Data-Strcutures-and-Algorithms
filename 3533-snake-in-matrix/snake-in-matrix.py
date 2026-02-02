class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        r,c = 0,0

        direction = {
            'RIGHT': (0,1),
            'LEFT': (0,-1),
            'UP': (-1,0),
            'DOWN': (1,0)
        }

        for command in commands: 
            dr, dc = direction[command]
            r += dr
            c += dc

        return r * n + c