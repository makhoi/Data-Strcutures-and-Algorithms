class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def isCuttable(m):
            cur = 0
            count = 0
            for sweet in sweetness:
                cur += sweet
                if cur >= m:
                    count += 1
                    cur = 0
            return count >= k + 1

        l , r = min(sweetness), sum(sweetness) // (k + 1)

        while l < r:
            m = (r + l + 1) // 2
            if isCuttable(m):
                l = m 
            else:
                r = m - 1
        
        return r
