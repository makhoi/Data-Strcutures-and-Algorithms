class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        '''
              l
              r
        2,1,4,3,5

        k = 10

        sum = 0


        START: 
        l = 0 
        r = 0
        [2]
        sum = 0 + 2 = 2
        score = 2*(r-l+1) = 2*(0-0+1) = 2 < k
        count = 1

        l = 0 
        r = 1
        [2, 1]
        sum = 2 + 1 = 3
        score = 3*(r-l+1) = 3*(1-0+1) = 3*2 = 6 < k
        count = 3

        l = 0
        r = 2
        [2,1,4]
        sum = 3 + 4 = 7
        score = 7*(r-l+1) = 7*3 = 21 >= k 
        [1,4]
        sum = 7 - 2 = 5 
        l = 1
        r = 2
        score = 5*2 = 10 >= k
        [4]
        sum = 5 - 1 = 4
        l = 2
        r = 2 
        score = 4*1 = 4 < k
        add = 1 
        count = 3 + 1 = 4

        l = 2 
        r = 3
        [4,3]
        sum = 7
        score = 7*2 = 14 >= k
        sum = 3
        [3]
        l = 3
        r = 3 
        score = 3 < k
        count = 4 + 1 = 5

        l = 3
        r = 4
        [3,5]
        sum = 3 + 5 = 8 
        score = 8*2 = 16 >= k
        sum = 8 - 3 = 5
        l = 4
        [5]
        score = 5*1 = 5 < k
        count = 5 + 1 = 6
        '''
        l = 0
        sum = 0 
        count = 0

        for r in range(len(nums)):
            sum += nums[r]

            while sum*(r-l+1) >= k and l <= r:
                sum -= nums[l]
                l += 1
            
            count += r - l + 1

        return count
