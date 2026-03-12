# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        '''
        0. Why is this binary search ? 
        a/ Search space increasing? yes
        b/ Continuous characteristic? yes

        1. Determine lowerbound / upperbound? 
        no duplicate -> lowerbound

        2. Determine search space? 
        index: 0 -> n

        3. Determine condition (move right): 
        if pick <= num

        4. Determine meaning of left after while loop: 
        min l satifies if pick <= num

        5. Determine result
        return pick
        '''
        l = 1
        r = n

        while l < r: 
            m = l + (r-l)//2

            if guess(m) <= 0:
                r = m
            else:
                l = m + 1
                
        return l