class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        '''
        0. Define binarsy search type basic/modified/adhoc: adhoc
        1. Lowerbound vs Upperbound: apply the bool function returning T/F: it will be FFFFFTTTTTT -> Find the first T 
        --> lowerbound
        2. Search space: 1 , max(nums)
        3. Condition to move right: if function return True else move left to mid + 1
        4. Meaning of left: min left satisfies the condition
        5. Return left
        '''
        def isSumLessThanThreshold(k):
            total = 0
            for num in nums:
                total += num//k
                if num%k != 0:
                    total += 1
            return total <= threshold

        left = 1
        right = max(nums)

        while left < right:
            mid = left + (right - left)//2

            if isSumLessThanThreshold(mid):
                right = mid
            else:
                left = mid + 1
        
        return left