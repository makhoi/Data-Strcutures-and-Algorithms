class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        l = len(nums)

        right_average = [0]*l
        right_average[l-1] = 101
        n = 1
        right_total = nums[l-1]

        for i in range(l-2, -1, -1):
            right_average[i] = right_total / n
            right_total += nums[i]
            n += 1
        
        res = 0
        for i in range(l):
            if nums[i] > right_average[i]:
                res += 1

        return res