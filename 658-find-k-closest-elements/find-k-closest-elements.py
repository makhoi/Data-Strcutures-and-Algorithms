class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        1. lowerbound vs upperbound: duplicate -> upperbound
        2. search space: 0 -> n-k : we are searching a window not just a value
        3. condition: 
        4. meaning of left/right: 
        5. result: 
        '''
        n = len(arr)
        l = 0
        r = n - k

        while l < r: 
            m = (r+l)//2
            if x - arr[m] > arr[m+k] - x: 
                l = m + 1
            else: 
                r = m
        return arr[l:l+k] 
