class Solution:
    def search(self, nums: List[int], target: int) -> int:
            
        # first find index of min value
        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        
        minIndex = left

        # define binary search function
        def binarySearch(start, end, find):
            while start < end:
                middle = start + (end-start)//2

                if find <= nums[middle]:
                    end = middle
                else:
                    start = middle + 1
            return start if nums[start] == find else -1

        if target <= nums[n-1]:
            return binarySearch(minIndex, n-1, target)
        else:
            return binarySearch(0, minIndex-1, target)