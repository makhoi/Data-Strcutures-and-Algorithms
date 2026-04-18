class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            mid = left + (right-left)//2

            if guess(mid) <= 0:
                right = mid
            else:
                left = mid + 1

        return left