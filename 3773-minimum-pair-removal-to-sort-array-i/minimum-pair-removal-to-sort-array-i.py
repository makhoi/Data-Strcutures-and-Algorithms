class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0

        while nums != sorted(nums): 
            smallest_pair = float('inf')
            smallest_index = -1
            for i in range(len(nums) - 1):
                current_pair = nums[i] + nums[i+1]
                if current_pair < smallest_pair:
                    smallest_pair = current_pair
                    smallest_index = i

            nums[smallest_index] = smallest_pair
            nums.pop(smallest_index + 1)
            count += 1
            
        return count