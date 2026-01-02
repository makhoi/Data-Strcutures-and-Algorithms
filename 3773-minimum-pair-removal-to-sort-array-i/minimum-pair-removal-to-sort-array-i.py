class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        '''
        If the list is not sorted
            Generate  sum of every subarray of elements with 2 numbers from nums: nums[i] + nums[i+1]
            Find out min_sum or the current list
            Find out the pair with smallest value
            Replace that pair with the its own sum
        count = 0
        Increase every time we did the replacements 
        return the count
        '''
        count = 0
        while nums != sorted(nums): 
            min_sum = float("inf")
            startIdx = 0
            for i in range(len(nums)-1):
                curr_sum = nums[i] + nums[i+1]
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    startIdx = i
                # min_sum
                
            # nums[startIdx] + nums[startIdx+1] = min_sum

            # Replace that pair with the its own sum
            nums[startIdx] = min_sum 
            nums.pop(startIdx+1)
            count += 1          

        return count