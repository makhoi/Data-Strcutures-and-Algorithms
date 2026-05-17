class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
            
        def can_divide(x):
            total_pile = 0
            for pile in candies:
                total_pile += pile // x
            return total_pile >= k
        
        left = 1
        right = max(candies)

        while left < right:
            mid = right - (right - left) // 2

            if can_divide(mid):
                left = mid
            else:
                right = mid - 1
        return left