from math import gcd
from math import lcm

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_product = [0]*n
        prefix_product[0] = nums[0]
        for i in range(1, n):
            prefix_product[i] = prefix_product[i-1]*nums[i]

        def prod(start, end):
            return prefix_product[end] // (prefix_product[start-1] if start else 1)

        def gcd_array(start, end): 
            g = nums[start]

            for i in range(start + 1, end + 1):
                g = gcd(g, nums[i])
            
            return g

        def lcm_array(start, end):
            m = nums[start]

            for i in range(start + 1, end + 1):
                m = lcm(m, nums[i])

            return m

        res = float('-inf')
        for i in range(n):
            for j in range(i+1, n):
                if prod(i,j) == gcd_array(i,j)*lcm_array(i,j):
                    res = max(res, j - i + 1)

        return res