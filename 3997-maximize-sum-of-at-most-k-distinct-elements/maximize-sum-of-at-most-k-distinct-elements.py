class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        '''
        1. First sort nums into descending order
        2. While k != 0, add num into set result with if num not in the set
        3. Decrease k by 1
        4. return result
        '''
        sorted_nums = sorted(nums, reverse=True)
        s = []
        for num in sorted_nums:
            if num not in s:
                s.append(num)
                k -= 1
                if k == 0:
                    break
        
        return s
