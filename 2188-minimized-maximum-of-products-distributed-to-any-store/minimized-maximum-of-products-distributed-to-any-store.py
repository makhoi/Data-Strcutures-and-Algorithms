class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        def can_distribute(x):
            stores_needed = 0
            for quantity in quantities:
                stores_needed += (quantity + x - 1) // x
            return stores_needed <= n
        
        left = 1
        right = max(quantities)

        while left < right:
            mid = left + (right - left) // 2

            if can_distribute(mid):
                right = mid
            else:
                left = mid + 1
        return left