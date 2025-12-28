class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        occurences = {}
        for num in nums:
            occurences[num] = occurences.get(num, 0) + 1

        for occurence in occurences.values(): 
            if occurence >= 2:
                return True
        return False
        