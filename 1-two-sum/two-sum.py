class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        num1 + num2 = target
        -> target - num2 = num1
        '''
        indices = {}

        for index, number in enumerate(nums):
            diff = target - number
            if diff in indices: 
                return [indices[diff], index]   
            indices[number] = index     
