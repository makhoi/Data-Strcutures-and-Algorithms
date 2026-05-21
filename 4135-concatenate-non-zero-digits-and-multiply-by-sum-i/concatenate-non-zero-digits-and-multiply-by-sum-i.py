class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0

        number = str(n)

        non_zeros = []
        for num in number:
            if num != '0':
                non_zeros.append(num)

        x = int("".join(non_zeros))
        
        s = 0
        for num in non_zeros:
            s += int(num)

        return x*s