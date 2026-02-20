class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        l
               r
        10,5,2,6

        product = 1
        count = 0

        Start: 
        l = 0
        r = 0
        [10]
        product = 1*10 = 10 < k 
        count = 1

        add 1 element -> len of window = 1 -> count + 1

        l = 0
        r = 1
        [10, 5]
        product = 10*5 = 50 < k 
        count = 1 + 2 = 3

        add 1 element - len of window = 2 -> count + 2

        l = 0
        r = 2
        [10, 5, 2]
        product = 50*2 = k -> shrink from left
        l = 1
        r = 2
        [5,2]
        product = 100/10 = 10
        count = 3 + 2 = 5

        add 1 element - len of window = 2 -> count + 2

        l = 1
        r = 3
        [5,2,6]
        product = 10*6 = 60 < k
        count = 5 + 3 = 8

        add 1 element - len of window = 3 -> count +3

        pattern:
        --> count += len of the window = r - l + 1
        '''
        l = 0
        product = 1
        count = 0

        for r in range(len(nums)):
            product *= nums[r]

            while product >= k and l <= r:
                product = product // nums[l]
                l += 1
            
            count += r - l + 1
        
        return count