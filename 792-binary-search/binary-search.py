# upperbound method
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            mid = right - (right-left)//2

            if target >= nums[mid]:
                left = mid
            else:
                right = mid - 1
        
        return -1 if nums[right] != target else right