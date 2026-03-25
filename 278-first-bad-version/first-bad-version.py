# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        '''
        TTTTTTFFFFFFFFF
        l      m      r
        '''

        '''
        0. basic/modified/adhoc: can be turn into array with Ts and Fs -> adhoc 
        1. lowerbound vs upperbound: find first F -> first appearance of target -> lowerbound
        2. search space: version 1 -> n
        3. condition to move right: if isBadVersion(mid) == True (first bad version)
        4. meaning of left: min left satisfies the condition
        5. return left
        '''

        left = 1
        right = n

        while left < right: 
            mid = left + (right - left)//2

            if isBadVersion(mid) == True: 
                right = mid
            else: 
                left = mid + 1
        return left