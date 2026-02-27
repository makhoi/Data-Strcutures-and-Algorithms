# Time: O(n)
# Sliding Window type 1
# Optimization from first attempt: update max frequency every time added a new nums[r] -> avoid max(dict) -> O(n^2) to O(n)
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        max_frequency = 0
        count = {}

        for r in range(len(nums)):
            count[nums[r]] = count.get(nums[r], 0) + 1
            max_frequency = max(max_frequency, count[nums[r]])

            while (r-l+1) - max_frequency > k:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]]
                l += 1
            
            res = max(res, max_frequency)

        return res