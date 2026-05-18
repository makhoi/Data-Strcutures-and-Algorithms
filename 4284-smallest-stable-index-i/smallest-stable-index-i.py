class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        left_maxes = [0]*n
        left_max = nums[0]
        for i in range(n):
            if nums[i] > left_max:
                left_max = nums[i]
            left_maxes[i] = left_max

        
        right_mins = [0]*n
        right_min = nums[n-1]
        for i in range(n - 1, -1, -1):
            if nums[i] < right_min:
                right_min = nums[i]
            right_mins[i] = right_min

        for i in range(n):
            instability_score = left_maxes[i] - right_mins[i]
            if instability_score <= k:
                return i

        return -1