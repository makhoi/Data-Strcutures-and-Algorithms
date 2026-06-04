class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        left_sum = [0]*n
        left_sum[0] = nums[0]

        total = sum(nums)
        right_sum = [0]*n
        right_sum[0] = total - left_sum[0]

        for i in range(1, n-1):
            left_sum[i] = left_sum[i-1] + nums[i]
            right_sum[i] = total - left_sum[i]
        
        count = 0
        for i in range(n-1):
            if (left_sum[i] - right_sum[i]) % 2 == 0:
                count += 1

        return count 