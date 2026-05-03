class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        '''
        ps[i] = s
        ps[j->i] = k
        ps[j-1] = s - k
        '''
        res = 0
        prefix_index = {}
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]

            if sum == k:
                res = max(res, i + 1)
            
            if sum - k in prefix_index:
                jM1 = prefix_index[sum-k]
                j = jM1 + 1
                res = max(res, i - j + 1)
            
            if sum not in prefix_index:
                prefix_index[sum] = i

        return res