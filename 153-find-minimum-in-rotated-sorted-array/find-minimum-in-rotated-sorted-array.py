class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        0. which type: basic/modified/adhoc? array gradually increasing and being modifed -> modified
        1. lowerbound vs upperbound? find min -> find first appearance of target? ->  lowerbound
        2. search space: index ranges from [0, n-1]
        3. condition to move right: if mid belongs to the second half -> if nums[mid] <= nums[n-1]
        4. meaning of left after exiting the while loop: min left satisfies the fcondtion if nums[left] <= nums[n-1] -> min value 
        5. result: return nums[left]
        '''
        n = len(nums)
        left = 0
        right = n - 1

        while left < right: 
            mid = left + (right - left)//2

            if nums[mid] <= nums[n-1]:
                right = mid
            else:
                left = mid + 1
        return nums[left]