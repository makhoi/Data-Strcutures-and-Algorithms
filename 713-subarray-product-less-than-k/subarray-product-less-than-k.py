class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''

           l
               r
        10,5,2,6
        
        k = 100

        count = 0
        
        product = 1

        Start:
        l = 0
        r = 0
        product = 1*10 = 10 < 100
        count = 1
        [10]

        l = 0
        r = 1
        product = 10*5 = 50 < 100 
        count = 2 
        [10,5] => [5] [10,5]

        l = 0
        r = 2
        [10,5,2] -> invalid subarray
        product = 50*2 = 100 = 100 (invalid)

        product = current_product/nums[l] = 100/10 = 10 (thoa dk)
        l += 1 = 1
        [5,2] => [2] [5,2]
        count = 3
        
        l = 1
        r = 3
        [5,2,6] =>  [6] [2,6] [5,2,6]
        product = 10*6 = 60 (Thoa dk)
        count = 4

        '''
        l = 0
        count = 0
        product = 1
        '''
        1,2,3
        k = 0 

        l = 0
        r = 0
        product = 1*1 = 1 >= k = 0 -> enter while
        product = 1/1 = 1
        count = 0

        l = 1 
        r =


        '''

        for r in range(len(nums)):
            product *= nums[r]

            while product >= k and l <= r:
                product = product / nums[l]
                l += 1

            count += r - l + 1

        return count