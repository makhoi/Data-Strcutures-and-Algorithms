class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        '''
        0. Convert integer to string to be able to traverse
        1. Create a hashmap called frequency to store frequency of each integer in the number
        2. Create another hashmap called ... where key is the frequency and value is the list of number with that frequency
        3. Find the smallest key in the table and return min(value) of that key
        '''
        nums = str(n)

        frequencies = {}
        for num in nums: 
            frequencies[num] = frequencies.get(num, 0) + 1

        frequency_to_nums = defaultdict(set)
        for num, frequency in frequencies.items():
            frequency_to_nums[frequency].add(num)
        
        # find the smallest frequency in frequency_to_nums table:
        smallest_frequency = float('inf')
        for f, num in frequency_to_nums.items():
            if f < smallest_frequency:
                smallest_frequency = f

        return int(min(frequency_to_nums[smallest_frequency]))