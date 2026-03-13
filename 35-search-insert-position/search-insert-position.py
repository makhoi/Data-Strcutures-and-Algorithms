class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        0. Binary search? Yes
        1. lowerbound vs upperbound? no dup -> lowerbound
        2. search space: 0 -> n
        3. condition: if nums[mid] >= target 
        4. meaning: min l satisfies condition
        5. result: l
        '''
        n = len(nums)
        l = 0
        r = n

        while l < r: 
            m = l + (r-l)//2

            if nums[m] >= target: 
                r = m
            else: 
                l = m + 1
        return l
