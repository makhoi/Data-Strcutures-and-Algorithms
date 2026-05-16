class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = float('inf')
        for i in range(len(nums)):
            if nums[i] < min:
                min = nums[i]
        return min
            
        