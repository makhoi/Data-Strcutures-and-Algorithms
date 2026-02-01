class Solution:
    def removeZeros(self, n: int) -> int:
        nums = str(n)
        result = []
        for num in nums:
            if num != '0':
                result.append(num)
        return int("".join(result))