class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        binary search: 
        - Dạng tìm element - no dup - either upperbound or lowerbound is fine
        - Modified binary search
        lowerbound vs upperbound: lowerbound
        search space: 0 -> n-1
        condition to move right: if target <= nums[mid]
        return nums[left] if nums[left] == target else -1
        '''
        n = len(nums)
        left = 0
        right = n-1

        while left < right:
            mid = left + (right-left)//2

            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        
        index_min_value = left

        def binarySearch(start, end, find):
            while start < end:
                mid = start + (end-start)//2

                if find <= nums[mid]:
                    end = mid
                else:
                    start = mid + 1

            return -1 if nums[start] != find else start

        if target <= nums[n-1]:
            return binarySearch(index_min_value, n-1, target)
        else:
            return binarySearch(0, index_min_value-1, target)
