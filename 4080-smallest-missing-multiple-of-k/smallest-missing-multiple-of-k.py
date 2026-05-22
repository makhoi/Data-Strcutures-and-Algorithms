class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)

        current = k
        while current in nums_set:
            current += k
        return current