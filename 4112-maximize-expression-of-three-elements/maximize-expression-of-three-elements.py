class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        '''
        maximize = a and b are 2 largest values and c is smallest value 9 in case this is all positive values)
        if there is negative:
            c is the smallest negative value
        '''
        smallest = min(nums)

        n = sorted(nums)
        two_largests = []
        for i in range(len(n) - 1, len(n) - 3, -1):
            two_largests.append(n[i])

        s = sum(two_largests)

        return s - smallest