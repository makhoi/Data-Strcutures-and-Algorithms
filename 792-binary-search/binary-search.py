class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        0. Decide which pattern to go for:
        - Search space increases from 0 -> x
        - Contiguous
        => Binary Search

        1. Decide lowerbound or upperbound:
        - No duplicate -> either works -> lowerbound now

        2. Define search space: (0, len(nums)-1)

        3. Define condition: 
        if target <= nums[mid]: r = mid

        4. Define meaning of left (right if we do upperbound): min l satifies condition 

        5. Return l
        '''
        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            mid = left + (right-left) // 2

            if target <= nums[mid]:
                right = mid

            else:
                left = mid + 1

        return -1 if target != nums[left] else left