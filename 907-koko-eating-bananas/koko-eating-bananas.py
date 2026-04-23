class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canEatWithinHHours(k):
            total = 0
            for pile in piles:
                total += pile // k 
                if pile % k != 0:
                    total += 1
            return total <= h

        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2

            if canEatWithinHHours(mid):
                right = mid
            else:
                left = mid + 1
        
        return left