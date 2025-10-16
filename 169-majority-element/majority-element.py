class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurence = {}
        for i in range(len(nums)):
            if nums[i] not in occurence:
                occurence[nums[i]] = 1
            else: 
                occurence[nums[i]] += 1

        for element, value in occurence.items(): 
            if value > len(nums)/2:
                return element