class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] > (nums[i-1] if i else float('-inf')) and nums[i] > (nums[i+1] if i != len(nums)-1 else float('-inf')):
                return i