class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0

        number = str(n)

        non_zeros = []
        for num in number:
            if num != '0':
                non_zeros.append(int(num))

        x = int("".join(map(str, non_zeros)))
        s = sum(non_zeros)

        return x*s