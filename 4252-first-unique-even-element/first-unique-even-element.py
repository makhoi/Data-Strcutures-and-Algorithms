class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        number_frequency = {}
        for num in nums:
            number_frequency[num] = number_frequency.get(num, 0) + 1

        for num in nums:
            if num % 2 == 0 and number_frequency[num] == 1:
                return num
        return -1