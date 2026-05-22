class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        smallest = min(nums)
        largest = max(nums)

        full = []
        for i in range(smallest, largest + 1):
            full.append(i)
        
        res = []
        for num in full:
            if num not in nums:
                res.append(num)
        
        return res