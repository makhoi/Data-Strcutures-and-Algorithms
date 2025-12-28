class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length_record = []
        length = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                length += 1
            if nums[i] == 0 or i == len(nums) - 1:
                length_record.append(length)
                length = 0
        return max(length_record)
        