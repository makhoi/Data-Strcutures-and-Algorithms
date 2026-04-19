class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEat(speed):
            total = 0

            for pile in piles:
                total += pile // speed
                if pile%speed != 0:
                    total += 1
            return total <= h

        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right-left)//2

            if canEat(mid) == True:
                right = mid
            else:
                left = mid + 1
        
        return left