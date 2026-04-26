class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        full = set()
        for num in range(min(nums), max(nums)+1):
            full.add(num)

        missing = []
        for num in full:
            if num not in nums:
                missing.append(num)
                
        return sorted(missing)