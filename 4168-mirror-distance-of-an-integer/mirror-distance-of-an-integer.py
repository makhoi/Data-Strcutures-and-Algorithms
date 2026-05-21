class Solution:
    def mirrorDistance(self, n: int) -> int:
        
        def reverse(k):
            number = str(k)
            reverse_number = []
            for i in range(len(number) - 1, -1, -1):
                reverse_number.append(number[i])
            return int("".join(reverse_number))

        return abs(n - reverse(n))