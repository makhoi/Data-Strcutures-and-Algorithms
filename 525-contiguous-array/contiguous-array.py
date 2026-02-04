class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''
        Lets say we have an array of -1s and 1s -> ps[j,i] = -1s + 1s = 0 -> đưa về dạng j,i có tổng k = 0
        '''
        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                nums[i] = -1

        max_length = 0
        prefix_map = {}
        prefix_sum = 0
        # k = 0

        for i in range(n):
            prefix_sum += nums[i]

            if prefix_sum == 0:
                max_length = max(max_length, i + 1)

            if prefix_sum in prefix_map:
                jM1 = prefix_map[prefix_sum]
                j = jM1 + 1
                l = i - j + 1
                max_length = max(max_length, l)

            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i

        return max_length