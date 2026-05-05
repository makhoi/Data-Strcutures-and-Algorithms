class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0]*n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        def leftSum(m):
            return prefix_sum[m-1] if i else 0

        def rightSum(m):
            return prefix_sum[n-1] - prefix_sum[m]

        for i in range(n):
            if leftSum(i) == rightSum(i):
                return i
        return -1