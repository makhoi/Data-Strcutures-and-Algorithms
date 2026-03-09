class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        # 1. define search space (left, right)
        0 -> n
        # 2. define contidion(mid)
        # if nums[mid] >= target: 
            r = mid 
        # 3. define left meaning after while loop
        # nums[left] >= target and left is minimum
        '''
        n = len(nums)
        l = 0
        # r = n - 1
        r = n # test case phải cover tất cả trường hợp --> 0 -> n -> r = n

        while l < r: 
            mid = l + (r-l) // 2 # lowerbound 

            if nums[mid] >= target:
                r = mid
            
            else: 
                l = mid + 1

        return l