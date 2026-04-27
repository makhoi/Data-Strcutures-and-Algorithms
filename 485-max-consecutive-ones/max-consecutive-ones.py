class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        num0 = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                num0 += 1
            
            while num0 == 1:
                if nums[left] == 0:
                    num0 -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res