class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_index = {}
        sum = 0
        jM1 = 0

        for i in range(len(nums)):
            sum += nums[i]

            if sum == k:
                res = max(res, i + 1)

            if sum - k in prefix_index:
                jM1 = prefix_index[sum-k]
                j = jM1 + 1
                length = i - j + 1
                res = max(res, length)

            if sum not in prefix_index:
                prefix_index[sum] = i
            
        return res