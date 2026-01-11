class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        smallest = min(nums)
        largest = max(nums)
        full = []
        for num in range(smallest, largest+1):
            full.append(num)

        original = set(nums)
        missing = []
        for num in full: 
            if num not in original: 
                missing.append(num)
        
        return missing
