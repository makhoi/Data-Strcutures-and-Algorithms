class Solution:
    def countElements(self, nums: List[int]) -> int:
        largest = max(nums)
        smallest = min(nums)

        count = 0
        for num in nums:
            if num < largest and num > smallest:
                count += 1
        return count