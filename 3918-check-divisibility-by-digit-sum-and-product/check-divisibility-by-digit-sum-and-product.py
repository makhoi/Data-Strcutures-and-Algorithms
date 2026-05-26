class Solution:
    def checkDivisibility(self, n: int) -> bool:
        numbers = str(n)
        addition = 0
        product = 1
        for num in numbers:
            addition += int(num)
            product *= int(num)

        total = addition + product
        if n % total == 0:
            return True
        return False