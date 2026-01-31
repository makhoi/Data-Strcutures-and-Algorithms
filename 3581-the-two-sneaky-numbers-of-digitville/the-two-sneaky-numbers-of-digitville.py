class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        num_frequency = {}
        for num in nums:
            num_frequency[num] = num_frequency.get(num, 0) + 1

        sneaky_numbers = []
        for num, frequency in num_frequency.items():
            if frequency == 2:
                sneaky_numbers.append(num)
        
        return sneaky_numbers