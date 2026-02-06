class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''
        When 1s = 0s -> 1s - 0s = 0 -> diff = 0 -> d = 0
        ps[i] = S
        ps[j,i] = d = 0
        ps[j-1] = S - d = S - 0 = S
        '''
        prefix_sum = 0
        prefix_map = {}
        max_length = 0
        n = len(nums)
        diff = 0

        for i in range(n):
            # prefix_sum += nums[i]

            if nums[i] == 1:
                diff += 1
            else:
                diff -= 1

            if diff == 0:
                max_length = max(max_length, i + 1)

            if diff in prefix_map:
                jM1 = prefix_map[diff]
                j = jM1 + 1
                l = i - j + 1
                max_length = max(max_length, l)

            if diff not in prefix_map:
                prefix_map[diff] = i

        return max_length
