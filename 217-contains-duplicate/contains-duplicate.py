class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        integer_frequency = {}
        for num in nums:
            integer_frequency[num] = integer_frequency.get(num, 0) + 1
            if integer_frequency[num] == 2:
                return True
        return False