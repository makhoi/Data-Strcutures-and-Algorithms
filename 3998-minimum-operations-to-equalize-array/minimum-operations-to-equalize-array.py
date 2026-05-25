class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) != 1:
            return 1
        return 0