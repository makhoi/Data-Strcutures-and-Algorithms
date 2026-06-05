class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_difference = float('-inf')
        for i in range(len(nums) - 1):
            max_difference = max(max_difference, abs(nums[i] - nums[i+1]))
        max_difference = max(max_difference, abs(nums[0] - nums[len(nums) - 1]))

        return max_difference