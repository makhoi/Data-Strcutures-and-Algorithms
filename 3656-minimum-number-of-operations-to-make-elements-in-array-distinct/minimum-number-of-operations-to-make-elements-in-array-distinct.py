class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == len(set(nums)):
            return 0

        operation = 0
        while(len(nums) != len(set(nums))): 
            if len(nums) >= 3:
                for _ in range(3):
                    nums.remove(nums[0])
                operation += 1
            else: 
                for _ in range(len(nums)-1):
                    nums.remove(nums[0])
                operation += 1

        return operation