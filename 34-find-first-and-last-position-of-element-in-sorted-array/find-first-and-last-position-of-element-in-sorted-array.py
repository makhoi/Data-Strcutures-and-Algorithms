class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        find first element -> lowerbound 
        find last element -> upperbound
        '''
        if not nums:
            return [-1, -1]

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left)//2

            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        
        leftRes = left

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = right - (right - left) // 2

            if target >= nums[mid]:
                left = mid
            else:
                right = mid - 1

        return [leftRes, right] if nums[leftRes] == target and nums[right] == target else [-1,-1]