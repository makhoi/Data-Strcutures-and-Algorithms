'''
Taị sao xài binary search?
1. Search space tăng dần 0 -> x
2. Tính liên tiếp: 
a) mid^2 < x^2 => (any number < mid)^2 < x^2
b) mid^2 > x^2 => (any number > mid)^2 > x^2
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        # 1. decide lowerbound vs upperbound
        search space without duplicate --> any works but prefer lower bound because its ezier
        search space with duplicates and find the latest target --> only upperbound works
        ==> no dup --> lowerbound

        # 2. define search space (left, right)
        0 -> x -> 0 -> n + 1
        # 3. define contidion(mid)
        if nums[mid]**2 >= x: 
            l = mid
        # 4. define left meaning after while loop
        min l satisfies l^2 >= x 
        # 5. what to return
        return l 
        '''
        # nums = []
        # for num in range(x):
        #     nums.append(num)

        l = 0
        r = x

        while l < r: 
            mid = l + (r-l) // 2

            if mid**2 >= x: 
                r = mid
            else: 
                l = mid + 1
        if l ** 2 == x:
            return l
        elif l ** 2 > x:
            return l - 1