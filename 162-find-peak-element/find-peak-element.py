class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        0. lowerbound vs upperbound: find the first element that is larger than its previous element -> lowerbound
        1. search space: index 0 -> len(nums)
        2. condition to move right: if nums[mid] >= nums[mid+1]
        3. meaning of left: min left satisfies the condition
        4. return left
        '''
        n = len(nums)
        left = 0
        right = n - 1

        while left < right: 
            mid = left + (right-left)//2

            if nums[mid] >= (nums[mid+1] if mid+1 <= n-1 else float('-inf')):
                right = mid
            else:
                left = mid + 1
                
        return left