class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        1. lowerbound vs upperbound: no dup -> lowerbound preferred
        2. search space: 0 -> n-1
        3. condition to move right: if nums[m] < nums[r]
        4. meaning of left after exiting the while loop: min l satisfies the condition
        5. result: if nums[l] == target -> return nums[l] else -1
        '''
        # find minimum in rotated sorted array
        n = len(nums)
        l = 0
        r = n-1

        while l < r: 
            m = l + (r-l)//2

            if nums[m] <= nums[r]: # midpoint belongs to the half right 
                r = m
            else: 
                l = m + 1
        
        minIndex = l # index of min value

        # the array is divided into 2 parts: 
        # right part: from minIndex -> n-1
        # left part: from 0 -> minIndex-1

        def binarySearch(left, right, find): 

            while left < right: 
                mid = left + (right-left)//2

                if nums[mid] >= find:
                    right = mid
                else: 
                    left = mid + 1

            return left if nums[left] == target else -1

        if target <= nums[n-1]:
            return binarySearch(minIndex, n-1, target)
        else: 
            return binarySearch(0, minIndex-1, target)