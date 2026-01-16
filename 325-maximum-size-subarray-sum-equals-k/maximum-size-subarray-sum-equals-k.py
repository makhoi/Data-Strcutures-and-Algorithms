class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefixMap = {}
        s = 0
        n = len(nums)
        res = 0

        for i in range(n):
            s += nums[i]

            if s == k: 
                res = max(res, i+1)

            # look back
            if s - k in prefixMap: 
                jM1 = prefixMap[s-k]
                j = jM1 + 1
                l = i - j + 1
                res = max(res, l)

            if s not in prefixMap:
                prefixMap[s] = i
        
        return res