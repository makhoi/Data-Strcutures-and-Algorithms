class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        frequencies = {}
        
        for num in nums: 
            frequencies[num] = frequencies.get(num, 0) + 1
        
        for frequency in frequencies.values():
            if frequency > 1:
                return True
        return False
