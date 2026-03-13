class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        1. lowerbound vs upperbound: no dup -> lowerbound
        2. search space: 0->n-1
        3. condition: 
        4. meaning of l: 
        5. result: 
        '''
        n = len(nums)
        l = 0 
        r = n - 1

        if nums[0] < nums[n-1]:
            return nums[0]
            
        while l < r: 
            m = l + (r-l)//2

            if nums[m] <= nums[r]: 
                r = m
            else: 
                l = m + 1
        return nums[l]