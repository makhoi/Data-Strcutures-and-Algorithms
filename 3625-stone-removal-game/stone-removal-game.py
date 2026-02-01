class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False

        turn = 0
        stone_remove = 10
        while n >= stone_remove:
            n -= stone_remove
            stone_remove -= 1
            turn += 1
        
        last_turn = turn
        if last_turn % 2 == 0:
            return False
        if last_turn % 2 == 1:
            return True