class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        occurences = {}
        for num in nums:
            occurences[num] = occurences.get(num, 0) + 1
        
        for val in occurences.values():
            if val >= 2:
                return True
        return False