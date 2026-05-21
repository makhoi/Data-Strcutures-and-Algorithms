class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        smallest = min(nums)

        n = sorted(nums)
        two_largests = []
        for i in range(len(n) - 1, len(n) - 3, -1):
            two_largests.append(n[i])

        s = sum(two_largests)

        return s - smallest