class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find minimum value
        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] <= nums[n-1]:
                right = mid
            else:
                left = mid + 1
        
        min_index = left

        # define binary search function
        def binarySearch(start, end):
            while start < end:
                mid = start + (end - start) // 2

                if nums[mid] >= target:
                    end = mid
                else:
                    start = mid + 1
            return start if nums[start] == target else -1

        # conduct binary search on each half
        if target <= nums[n-1]:
            return binarySearch(min_index, n-1)
        else:
            return binarySearch(0,min_index-1)

           