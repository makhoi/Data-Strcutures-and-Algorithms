class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        for num in range(min(nums), max(nums)):
            if num not in nums:
                res.append(num)
        return res
