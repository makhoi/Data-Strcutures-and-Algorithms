class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        1. Define approach:
        - search space: index increases from 0 -> len(nums) - 1
        - Consecutiveness
        => Binary Search problem

        2. Decide lowerbound vs upperbound: asking for both earlier appaearance and latter appearance 
        => lowerbound and upperbound

        3. Define search space: 
        index 0 -> len(nums) - 1

        4. Define condition(mid): 
        lowerbound: target <= nums[mid] -> right = mid
        upperbound: target >= nums[mid] -> left = mid

        5. Define meaning of left and right:
        left: min left satifies lowerbound condition
        right: max right satisfies upperbound condition
        '''

        n = len(nums)
        left = 0
        right = n - 1

        if n == 0:
            return [-1, -1]

        while left < right:
            mid = left + (right - left) // 2

            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1

        leftRes = left

        left = 0
        right = n - 1

        while left < right:
            mid = right - (right-left)//2

            if target >= nums[mid]:
                left = mid
            else:
                right = mid - 1
        
        return [-1,-1] if nums[leftRes] != target and nums[right] != target else [leftRes, right]