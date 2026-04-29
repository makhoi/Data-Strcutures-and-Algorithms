class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        number_frequency = {}
        left = 0
        
        for right in range(len(nums)):
            number_frequency[nums[right]] = number_frequency.get(nums[right], 0) + 1

            while number_frequency.get(0,0) == 2:
                number_frequency[nums[left]] -= 1
                if number_frequency[nums[left]] == 0:
                    del number_frequency[nums[left]]
                left += 1

            res = max(res, right - left + 1)

        return res