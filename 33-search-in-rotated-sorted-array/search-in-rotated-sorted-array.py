class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find index of the minimum element
        n = len(nums)
        left = 0
        right = n-1

        while left < right:
            mid = left + (right-left)//2

            if nums[mid] <= nums[right]:
                right = mid
            else: 
                left = mid + 1
        
        minIndex = left

        # write binary search function 
        def binarySearch(start, end, find): 
            while start < end: 
                midpoint = start + (end-start)//2

                if nums[midpoint] >= target: 
                    end = midpoint
                else: 
                    start = midpoint + 1
            return start if nums[start] == find else -1

        # conduct binary search
        if target <= nums[n-1]: 
            return binarySearch(minIndex,n-1,target)
        else: 
            return binarySearch(0,minIndex-1,target)