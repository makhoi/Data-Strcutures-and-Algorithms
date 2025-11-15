class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}

        for index, num in enumerate(nums):
            if num not in left:
                left[num] = index
            right[num] = index
            count[num] = count.get(num, 0) + 1
        
        ans = len(nums)
        degree = max(count.values())
        for value in count:
            if count[value] == degree:
                ans = min(ans, right[value] - left[value] + 1)
        return ans