class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0

        # Phase 1: strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        # p must exist, and first phase must not be empty
        if i == 0 or i == n - 1:
            return False

        # Phase 2: strictly decreasing
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1

        # q must exist, and second phase must not end at last index
        if i == n - 1:
            return False

        # Phase 3: strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        return i == n - 1