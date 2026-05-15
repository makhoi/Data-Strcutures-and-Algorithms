class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        '''
        in case there is no zero
        use binary search -> find first appearance of positive integer
        -> count of pos = len(nums) - left
        -> count of neg = left

        in case there are zeros:
        use lowerbound binary search to find first appearance of positive integer
        -> pos = len(nums) - left
        use upperbound bs to find last appearance of negative integer
        -> neg = right
        O(logn)
        '''
        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > 0:
                right = mid
            else:
                left = mid + 1
        if nums[left] <= 0:
            pos = 0
        else:
            pos = n - left

        left = 0
        right = n - 1

        while left < right:
            mid = right - (right - left) // 2

            if nums[mid] < 0:
                left = mid
            else:
                right = mid - 1
        if nums[right] >= 0:
            neg = 0
        else:
            neg = right + 1

        return max(pos, neg)