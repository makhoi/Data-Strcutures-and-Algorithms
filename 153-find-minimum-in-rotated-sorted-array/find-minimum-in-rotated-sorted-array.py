class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        find the minimum element
        '''
        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] <= nums[n-1]:
                right = mid
            else:
                left = mid + 1
                
        return nums[left]