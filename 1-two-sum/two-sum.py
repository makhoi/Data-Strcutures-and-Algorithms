class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for index, value in enumerate(nums):
            diff = target - value
            if diff not in dict: 
                dict[value] = index
            else: 
                return dict[diff], index
        