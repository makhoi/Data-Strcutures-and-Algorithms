class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0
        while nums != sorted(nums):
            min_sum = float('inf')
            startIdx = 0
            for i in range(len(nums)-1): 
                curr_num = nums[i] + nums[i+1]
                if curr_num < min_sum:
                    min_sum = curr_num
                    startIdx = i

            nums[startIdx] = min_sum
            nums.pop(startIdx+1)
            count += 1
            
        return count