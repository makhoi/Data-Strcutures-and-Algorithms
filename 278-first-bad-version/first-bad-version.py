class Solution:
    def firstBadVersion(self, n: int) -> int:
        '''
        find first bad version-> first True (to bad)
        '''
        left = 1
        right = n
        
        while left < right:
            mid = left + (right-left)//2

            if isBadVersion(mid) == True:
                right = mid
            else:
                left = mid + 1

        return left