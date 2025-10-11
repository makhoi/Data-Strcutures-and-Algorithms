class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target: 
                return i
        else: 
            nums.append(target)
            updated = sorted(nums)
            for j in range(len(updated)):
                if updated[j] == target: 
                    return j
            