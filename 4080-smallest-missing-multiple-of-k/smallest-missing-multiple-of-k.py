class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        full = []
        for num in range(k, max(nums)+ k + 1):
            if num % k == 0:
                full.append(num)
        
        for num in full:
            if num not in nums:
                return num