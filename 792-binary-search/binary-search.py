'''
Does this problem satisfy condition to use binary search? 
1. Search space increase? -1 -> 12 -> Yes 
2. Continuous behavior? 
mid_value < target -> any number < mid_value < target? Yes
mid_value > target -> any number > mid_value > target? Yes
==> Yes this problem satisfies to use binary search
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        1. Decide lowerbound vs upperbound? 
        Search space without duplicate -> both works but prefer lowercase because we are more familiar with it
        Search space with duplicates and find the latest integer -> upperbound
        => Search space without duplicate -> lowerbound
        
        2. Define search space (left, right)
        Index: 0 -> n-1

        3. Define condition (mid)
        if target <= nums[mid]

        4. Define left meaning after the while loop:
        min left satisfies condition if target <= nums[mid]

        5. Define what to return?
        return left if nums[left] == target else -1
        '''

        # naive way
        # begin_index = 0 # r
        # end_index = len(nums) - 1 # l 

        # while begin_index <= end_index: 
        #     mid_index = begin_index + (end_index - begin_index) // 2
        #     mid_point = nums[mid_index]

        #     if target == mid_point:
        #         return mid_index

        #     elif target < mid_point:
        #         end_index = mid_index - 1

        #     else: 
        #         begin_index = mid_index + 1

        # return -1

        n = len(nums)
        left = 0
        right = n - 1

        while left < right: 
            mid = left + (right - left) // 2

            if target <= nums[mid]: 
                right = mid
            else: 
                left = mid + 1
        
        return -1 if nums[left] != target else left
'''
1. Define lowerbound vs upperbound: no dup -> lowerbound
2. Define search space: index -> 0 -> 5
3. Define condition(mid): 
if target <= nums[mid]
4. Define meaning of left after while loop: 
min left satisfies target <= nums[mid] -> target = nums[left]
5. Define what to return: 
return left else -1 if nums[left] != target


[-1,0,3,5,9,12]
target = 9

START: 
l = 0
r = 5
     m l    r
-1,0,3,5,9,12
l < r -> yes
m = 0 + (5-0)//2 = 2
9 <= 3? nope -> l = m + 1 = 2 + 1 = 3

       l m r
-1,0,3,5,9,12
l < r -> yes 
m = l + (r-l)//2 = 3 + (5-3)//2 = 4
9 <= nums[m] = 9? yes
r = 4

l < r? nope -> exit while loop

nums[left] = 9 != target = 9? nope -> return left = 4
'''