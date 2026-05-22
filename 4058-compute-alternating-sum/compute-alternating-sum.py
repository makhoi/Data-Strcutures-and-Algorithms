class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        s = 0
        for i, n in enumerate(nums):
            s += n if i % 2 == 0 else -n
        return s