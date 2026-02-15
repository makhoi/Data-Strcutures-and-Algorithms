class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        '''
        find subarray that has length len(cardPoints) - k has the min sum
        '''
        l = 0
        min_sum = float('inf')
        n = len(cardPoints)
        current_sum = 0
        total = sum(cardPoints)

        for r in range(n):
            current_sum += cardPoints[r]

            while (r - l + 1) > (n - k):
                current_sum -= cardPoints[l]
                l += 1
            
            if r - l + 1 == n - k:
                min_sum = min(min_sum, current_sum)

        return int(total - min_sum)