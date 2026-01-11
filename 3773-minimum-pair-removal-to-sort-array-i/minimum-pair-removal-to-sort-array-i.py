class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0
        while nums != sorted(nums):
            min_sum = float('inf')
            startIndx = 0
            for i in range(len(nums)-1):
                curr_sum = nums[i] + nums[i+1]
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    startIndx = i
            
            nums[startIndx] = min_sum
            nums.pop(startIndx+1)
            count += 1
        
        return count
