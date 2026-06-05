class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        '''
        define prefix sum function
        define start for each index
        '''
        n = len(nums)
        prefix_sum = [0]*n
        prefix_sum[0] = nums[0]
        for i in range(1,n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        def rangeSum(left, right):
            return prefix_sum[right] - (prefix_sum[left-1] if left else 0)

        starts = []
        for i in range(n):
            starts.append(max(0, i - nums[i]))

        sums = []
        for i in range(n):
            sums.append(rangeSum(starts[i], i))

        return sum(sums)