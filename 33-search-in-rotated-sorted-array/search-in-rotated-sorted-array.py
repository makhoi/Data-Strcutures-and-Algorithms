class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        After being rotated, the array can be divided into 2 parts:
        - half left: left pointer -> index of max(nums)
        - right pointer: index of min(nums) -> right pointer 
        Then we can conduct search separately depends on where the target lies in

        TODO: 
        1. Find where the index of min(nums) is (refer to find minimum in rotated sorted array leetcode problem above)
        2. Write a binary search function taking 3 parameters (left, right, target) 
        3. Conduct binary search depends where the target is
        '''

        '''
        lowerbound vs upperbound: 
        search space: index 0 -> n-1

        '''

        # find the index of the minimum element in rotated sorted array 
        n = len(nums)
        left = 0
        right = n - 1

        while left < right: # why are we using lowerbound here 
            mid = left + (right - left)//2

            if nums[mid] <= nums[right]:
                right = mid
            else: 
                left = mid + 1

        minIndex = left

        # write binary search function 
        def binarySearch(start, end, find):
            while start < end: 
                midpoint = start + (end - start)//2

                if find <= nums[midpoint]:
                    end = midpoint
                else:
                    start = midpoint + 1
            return start if nums[start] == target else -1

        # conduct binary search depends on which half it belongs to
        if target <= nums[n-1]: # target lies on right half
            return binarySearch(minIndex, n-1, target)
        else:
            return binarySearch(0,minIndex-1,target)