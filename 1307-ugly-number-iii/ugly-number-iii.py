class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        '''
        answer from youtube
        '''
        a_b = a * b // math.gcd(a,b)
        b_c = b * c // math.gcd(b,c)
        a_c = a * c // math.gcd(a,c)
        a_b_c = (a_b*c) // math.gcd(a_b, c)

        def isFeasible(num):
            result = (num // a) + (num // b) + (num // c) - (num // a_b) - (num // b_c) - (num // a_c) + (num // a_b_c)
            return result >= n

        left = 1
        right = 2*10**9

        while left < right:
            mid = left + (right-left)//2

            if isFeasible(mid):
                right = mid
            else:
                left = mid + 1
        return left