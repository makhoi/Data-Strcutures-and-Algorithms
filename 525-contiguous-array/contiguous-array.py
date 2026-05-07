class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''
        Convert every 0s to -1s
        length 0s = length 1s <=> length -1s = length 1s <=> total = 0
        ps[i] = s
        ps[j...i] = 0
        ps[j-1] = s - 0 = s
        '''
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        
        res = 0
        jM1 = 0
        s = 0
        s_index = {}

        for i in range(n):
            s += nums[i]

            if s == 0:
                res = max(res, i + 1)

            if s in s_index:
                jM1 = s_index[s]
                j = jM1 + 1
                res = max(res, i - j + 1)

            if s not in s_index:
                s_index[s] = i

        return res