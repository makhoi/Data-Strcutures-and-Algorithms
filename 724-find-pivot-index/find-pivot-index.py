class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0]*len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)): 
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        total = prefix_sum[len(nums) - 1]

        for i in range(len(nums)): 
            if i == 0: 
                left_sum = 0
                right_sum = total - nums[i]
            elif i == len(nums) - 1:
                right_sum = 0
                left_sum = total - nums[i]
            else: 
                right_sum = total - prefix_sum[i]
                left_sum = prefix_sum[i-1]
            if right_sum == left_sum:
                return i 
        return -1