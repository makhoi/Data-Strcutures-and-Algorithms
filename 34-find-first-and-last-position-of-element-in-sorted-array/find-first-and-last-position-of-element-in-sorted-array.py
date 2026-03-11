class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        0. Why binary search? 
        Search space increase? index increase from 0->n-1 -> Yes
        Continuous? yes 

        1. Determine lowerbound vs upperbound? 
        Dup + find last element -> upperbound
        find first element -> lowerbound

        2. Determine search space: 
        0 -> n-1

        3. Determine condition: 
        a) lowerbound: 
        if target <= nums[mid]: 
        b) upperbound: 
        if target >= nums[mid]

        4. Determine meaning of
        a) lowerbound: left after exiting while loop 
        min l satifies if target <= nums[mid]
        b) upperbound: max after exiting while loop
        max r satifies target >= nums[mid]

        5. Determine result: 
        return [left, right]
        '''
        n = len(nums)
        l = 0
        r = n-1

        # special case: empty nums
        if len(nums) == 0:
            return [-1, -1]

        # lowerbound -> find first element 
        while l < r:
            m = l + (r-l) // 2

            if target <= nums[m]:
                r = m
            else: 
                l = m + 1
        
        first_element = l

        # upperbound -> find last element 
        l = 0
        r = n - 1

        while l < r: 
            m = r - (r-l)//2

            if target >= nums[m]:
                l = m
            else: 
                r = m-1
        
        last_element = r

        if nums[first_element] == nums[last_element] == target: 
            return [first_element, last_element]
        else:
            return [-1, -1]