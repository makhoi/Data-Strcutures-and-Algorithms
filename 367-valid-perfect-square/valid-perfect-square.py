class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num

        while l < r: 
            m = l + (r-l)//2

            if m**2 >= num: 
                r = m
            else: 
                l = m + 1

        if l**2 == num:
            return True
        elif l**2 > num:
            return False