class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k:
            smallest_value = float('inf')
            smallest_value_index = 0

            for index, num in enumerate(nums):
                if num < smallest_value:
                    smallest_value = num
                    smallest_value_index = index

            nums[smallest_value_index] = smallest_value*multiplier

            k -= 1
        
        return nums