class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1

        while left < right:
            mid = left + (right-left)//2

            left_size = mid - 1 if nums[mid] == nums[mid-1] else mid

            if left_size % 2 == 1:
                right = mid
            else: 
                left = mid + 1

        if left % 2 == 0:
            return nums[left]
        else:
            return nums[left-1] 