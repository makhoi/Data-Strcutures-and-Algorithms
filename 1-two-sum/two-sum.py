class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            # check first
            diff = target - num
            if diff in seen:
                return [index, seen[diff]]
            # insert
            seen[num] = index