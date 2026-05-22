class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)

        return [num for num in range(min(nums), max(nums) + 1) if num not in nums_set]