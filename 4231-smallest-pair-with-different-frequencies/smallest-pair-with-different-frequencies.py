class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        if len(nums) <= 2:
            return [-1,-1]

        number_frequency = {}
        for num in nums:
            number_frequency[num] = number_frequency.get(num, 0) + 1
        
        smallest = min(number_frequency)
        smallest_frequency = number_frequency[smallest]

        others = []
        for number, frequency in number_frequency.items():
            if number > smallest and frequency != smallest_frequency:
                others.append(number)

        if others == []:
            return [-1,-1]

        other = min(others)

        return [smallest, other]