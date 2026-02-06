class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''
        Method 2: Convert 0 to -1 

        ps[i] = S
        ps[j,i] = k = 0
        ps[j-1] = S - k = S - 0 = S
        '''
        prefix_sum = 0
        prefix_map = {}
        n = len(nums)
        max_length = 0

        for i in range(n):
            if nums[i] == 0:
                nums[i] = -1
            
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