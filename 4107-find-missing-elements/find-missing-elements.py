class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_val = min(nums)
        max_val = max(nums)

        existing = set(nums)
        missing = []

        for value in range(min_val + 1, max_val):
            if value not in existing:
                missing.append(value)

        return missing