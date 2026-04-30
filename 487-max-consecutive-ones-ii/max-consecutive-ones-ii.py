class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        number_frequency = {}
        left = 0

        for right in range(len(nums)):

            while number_frequency.get(0,0) == 1 and nums[right] == 0:
                if nums[left] == 0:
                    number_frequency[nums[left]] -= 1
                left += 1
            
            number_frequency[nums[right]] = number_frequency.get(nums[right], 0) + 1
            
            res = max(res, right - left + 1)

        return res