class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        total_flower = m*k

        if len(bloomDay) < total_flower: 
            return -1

        def can_bloom(day):
            bouquet = 0
            consecutive = 0

            for b in bloomDay:
                if b <= day:
                    consecutive += 1
                    if consecutive == k: 
                        bouquet += 1
                        consecutive = 0
                else: 
                    consecutive = 0
            return bouquet >= m

        left = min(bloomDay)
        right = max(bloomDay)

        while left < right: 
            mid = left + (right - left)//2

            if can_bloom(mid) == True:
                right = mid
            else:
                left = mid + 1

        return left