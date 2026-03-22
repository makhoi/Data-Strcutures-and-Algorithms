# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        '''
        0. basic/modified/adhoc: 
        - modified: array tăng dần và bị biến đổi ở đâu đó
        - adhoc: phải biến đổi đề thành array () 
        => Biến đổi thành GGGGBBBB -> FFFFTTTT 
        => adhoc
        1. lowerbound vs upperbound: lowerbound but why? there is duplicate 
        2. search space: 1 -> n
        3. condition to move right: isBadVersion(m) -> True 
        4. meaning of left: the first version that isBadVersion(m) returns True 
        5. result: returns l
        '''
        l = 1
        r = n

        while l < r: 
            m = l + (r-l)//2

            if isBadVersion(m) == True:
                r = m
            else: 
                l = m + 1
        
        return l
        