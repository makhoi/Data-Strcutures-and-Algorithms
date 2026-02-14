class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        num0 = 0

        for r in range(len(nums)):

            while num0 == k and nums[r] == 0:
                if nums[l] == 0:
                    num0 -= 1
                l += 1
            
            if nums[r] == 0:
                num0 += 1

            res = max(res, r - l + 1)

        return res
