class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        # convert integer n to string to be able to iterate over it
        nums = str(n)
        # num_to_frequency table to store frequency of each table
        num_to_frequency = {}
        for num in nums:
            num_to_frequency[num] = num_to_frequency.get(num, 0) + 1

        # frequency_to_nums table is basically opposite version of num_to_frequency where key: frequency, value: list of nums
        frequency_to_nums = defaultdict(set)
        for n,f in num_to_frequency.items():
            frequency_to_nums[f].add(n)

        # find the smallest frequency from frequency_to_nums table aka the smallest key in frequency_to_nums table
        smallest_frequency = float('inf')
        for f in frequency_to_nums.keys():
            if f < smallest_frequency:
                smallest_frequency = f

        # return the min value of that smallest frequency (convert it back to integer)
        return int(min(frequency_to_nums[smallest_frequency]))
        