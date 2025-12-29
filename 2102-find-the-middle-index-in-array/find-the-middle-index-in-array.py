class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0]*n
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        total = prefix_sum[n - 1]

        for i in range(n):
            right_sum = total - prefix_sum[i] if i != n - 1 else 0
            left_sum = prefix_sum[i-1] if i else 0
            if right_sum == left_sum:
                return i
        return -1