class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(set(nums), reverse = True)

        if k > len(nums):
            return nums
            
        res = []
        for i in range(k):
            res.append(nums[i])
        
        return res