class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        '''
        1. lowerbound vs upperbound: dup -> upperbound
        2. search space: 0 -> n-1
        3. condition to move right: leftSize % 2 == 1
        4. meaning of left after exiting the while loop: 
        5. result: nums[l]
        '''
        n = len(nums)
        l = 0
        r = n-1

        while l < r:
            m = l + (r-l)//2

            leftSize = m-1 if nums[m-1] == nums[m] else m
            if leftSize % 2 == 1:
                r = m
            else: 
                l = m + 1
                
        if l % 2 == 1:
            return nums[l-1]
        else: 
            return nums[l]