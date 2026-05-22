class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        full = list(range(min(nums), max(nums) + 1))
        
        res = []
        for num in full:
            if num not in nums:
                res.append(num)
        
        return res