class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        result = []

        for num in nums: 
            if num: 
                count += 1
            else: 
                result.append(count)
                count = 0
        result.append(count)

        return max(result)

        