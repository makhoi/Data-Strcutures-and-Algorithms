class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        right sum = total - prefix_sum[i] if i != len(nums) - 1 else 0
        left_sum = prefix_sum[i-1] if i else 0
        '''
        prefix_sum = [0]*len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        total = prefix_sum[len(nums) - 1]

        for i in range(len(nums)):
            left_sum = prefix_sum[i-1] if i else 0
            right_sum = total - prefix_sum[i] if i != len(nums) - 1 else 0
            if right_sum == left_sum:
                return i
        return -1