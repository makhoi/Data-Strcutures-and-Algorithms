class Solution:
    def removeZeros(self, n: int) -> int:
        return int("".join([num for num in str(n) if num != '0']))