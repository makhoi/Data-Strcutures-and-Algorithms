class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in two_sum:
                return [two_sum[diff], i]
            two_sum[nums[i]] = i
        