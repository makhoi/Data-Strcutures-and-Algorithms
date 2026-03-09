class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin_index = 0
        end_index = len(nums) - 1

        while begin_index <= end_index: 
            midpoint = (begin_index + end_index) // 2 # / là chia số real , // là chia số nguyên
            midpoint_value = nums[midpoint]

            if target == midpoint_value:
                return midpoint
            
            elif target < midpoint_value:
                end_index = midpoint - 1

            else: 
                begin_index = midpoint + 1
        return -1