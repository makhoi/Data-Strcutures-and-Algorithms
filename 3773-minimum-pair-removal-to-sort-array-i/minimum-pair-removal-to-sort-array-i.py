class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        '''
        1. If the nums is sorted -> return 0
        2. Set var min_sum = float('inf')
        3. Find the min_sum of the current array by running an index through the nums, curr_sum = nums[i] + nums[i+1]
        4. if curr_nums < min_sum, update that, also maintain a var startIndx
        5. replace min_sum with nums[startIndx]
        6. remove nums[startIndx]
        '''
        count = 0
        while nums != sorted(nums):
            min_sum = float('inf')
            curr_sum = 0    
            
            for i in range(len(nums) - 1):
                curr_sum = nums[i] + nums[i+1]
                
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    startIndx = i
            
            nums[startIndx] = min_sum
            nums.pop(startIndx+1)
            count += 1
        
        return count