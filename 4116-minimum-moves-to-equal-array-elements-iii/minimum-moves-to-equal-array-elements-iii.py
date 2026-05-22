class Solution:
    def minMoves(self, nums: List[int]) -> int:
        largest = max(nums)

        res = 0
        for i in range(len(nums)):
            res += largest - nums[i]

        return res