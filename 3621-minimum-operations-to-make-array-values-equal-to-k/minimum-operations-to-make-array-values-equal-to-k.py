class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if len(set(nums)) > 1 and max(nums) == k:
            return -1

        count = 0
        while len(set(nums)) != 1:
            h = sorted(set(nums))[-2]
            for i in range(len(nums)):
                if nums[i] > h:
                    nums[i] = h
            count += 1
        
        if nums[0] == k:
            return count
        elif nums[0] > k:
            return count + 1
        else:
            return -1