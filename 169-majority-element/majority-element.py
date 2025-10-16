class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurences = {}
        for num in nums: 
            occurences[num] = occurences.get(num, 0) + 1
        

        for element, occurence in occurences.items(): 
            if occurence > len(nums)/2:
                return element