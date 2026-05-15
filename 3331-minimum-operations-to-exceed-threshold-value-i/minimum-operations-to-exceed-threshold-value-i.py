class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        '''
        solve this using binary search:
        - sort the array
        - find the first appearance that is larger or equal to k
        '''
        nums = sorted(nums)

        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            mid = left + (right - left)//2

            if nums[mid] >= k:
                right = mid
            else:
                left = mid + 1
        return left