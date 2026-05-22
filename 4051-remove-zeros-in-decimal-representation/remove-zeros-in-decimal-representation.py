class Solution:
    def removeZeros(self, n: int) -> int:
        nums_str = str(n)

        return int("".join([num for num in nums_str if num != '0']))