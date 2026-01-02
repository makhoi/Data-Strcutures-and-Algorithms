class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        for element, f in frequency.items():
            if f == len(nums) // 2 and f == len(set(nums)) - 1:
                return element