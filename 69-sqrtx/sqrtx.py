class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        lowerbound vs upperbound: round down -> first appearance -> lowerbound
        search space: 0 -> x
        condition to move right: mid ** 2 >= x
        meaning of left: min left satisfies condition
        return mid
        '''
        left = 0
        right = x

        while left < right:
            mid = left + (right-left)//2

            if mid**2 >= x: 
                right = mid
            else:
                left = mid + 1
        
        if left ** 2 == x:
            return left
        else:
            return left - 1