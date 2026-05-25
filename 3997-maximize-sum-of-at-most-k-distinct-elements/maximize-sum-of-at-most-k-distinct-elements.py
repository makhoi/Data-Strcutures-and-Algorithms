class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)

        k_largest = []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] not in k_largest:
                k_largest.append(nums[i])
                k -= 1
            if k == 0:
                break
        
        return k_largest