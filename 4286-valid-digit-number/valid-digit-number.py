class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        integer = str(n)
        digit = str(x)

        if integer[0] == digit:
            return False

        for i in range(len(integer)):
            if integer[i] == digit:
                return True
        return False
