class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            if nums[i] == 0 or i == len(nums) - 1:
                res.append(count)
                count = 0
        return max(res)