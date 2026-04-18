class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n

        while left < right: 
            mid = right - (right-left)//2

            if (mid/2)*(mid+1) <= n:
                left = mid
            else:
                right = mid - 1

        return right