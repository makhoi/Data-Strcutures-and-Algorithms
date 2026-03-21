class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        1. lowerbound vs upperbound: no dup -> lowerbound preferred
        2. search space: 0 -> n-1
        3. condition to move right: when midpoint belongs to the right half of the rotated array,
        we move r pointer to the midpoint -> how to know when midpoint belongs to the right half of the array? when nums[m] < nums[r]
        Hence: if nums[m] < nums[r]: r = m
        4. meaning of left after exiting the while loop: min left satisfies the condition nums[l] < nums[r]
        5. result: min element -> nums[l]
        '''
        n = len(nums)
        l = 0
        r = n-1

        while l < r: 
            m = l + (r-l)//2

            if nums[m] <= nums[r]: # midpoint is in the half right -> move r to midpoint
                r = m
            else: # midpoint is in the half left -> move l to midpoint
                # l = m
                l = m + 1 # I forgot why is this m + 1 here? tạm thời cứ mặc định là vậy, đợi review dạng 1 ắt sẽ rõ

        return nums[l]