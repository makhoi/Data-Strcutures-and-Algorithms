class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, element in enumerate(nums):
            diff = target - element
            if diff not in hashmap: 
                hashmap[element] = index
            else: 
                return index, hashmap[diff]

        
        