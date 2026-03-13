class Solution:
    def search(self, nums, target):
        '''
        1. lowerbound vs upperbound: no dup -> lowerbound
        2. search space: 0->n-1
        3. condition: nums[mid] >= target
        4. meaning of l: 
        5. result: 
        '''
        n = len(nums)
        l = 0 
        r = n - 1

        # if nums[0] < nums[n-1]:
        #     return nums[0]

        while l < r: 
            m = l + (r-l)//2

            if nums[m] <= nums[r]: 
                r = m
            else: 
                l = m + 1   
        # chia array thành 2 đoạn:
        # right: min value -> giá trị nào đó x
        # left: giá trị y nào đó > max(right) -> max(nums) 

        minIndex = l
        
        def binarySearch(left, right, find): 

            while left < right: 
                mid = left + (right - left) // 2

                if nums[mid] >= find: 
                    right = mid
                else: 
                    left = mid + 1
            return left if nums[left] == target else -1

        if target <= nums[n-1]: # thuoc right array 
            return binarySearch(minIndex,n-1,target) 
        else: 
            # binary search tren left array
            return binarySearch(0,minIndex-1,target)
            