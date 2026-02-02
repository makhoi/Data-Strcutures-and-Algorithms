class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        max_length = 0
        prefix_map = {}
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum == k:
                max_length = max(max_length, i + 1)

            if prefix_sum - k in prefix_map:
                jM1 = prefix_map[prefix_sum - k]
                j = jM1 + 1
                l = i - j + 1

                max_length = max(max_length, l)

            if prefix_sum not in prefix_map: 
                prefix_map[prefix_sum] = i

        return max_length