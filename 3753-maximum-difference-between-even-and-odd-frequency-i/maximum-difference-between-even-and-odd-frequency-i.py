class Solution:
    def maxDifference(self, s: str) -> int:
        '''
        Find the maximum difference of odd and even frequency 
        -> max difference = max_frequency_odd - min_frequency_even 
        using 3 hashmaps
        first hashmap character_frequency to track frequency of the character_frequency
        second hashmap odd_frequency to store only character with odd frequency from the first hashmap 
        third hashmap even_frequency to store only character with even frequency from the first hashmap
        pick the key with max value from second table and key with min value from third table 
        max_diff = max(odd) - min(even)
        '''
        character_frequency = {}
        for ch in s:
            character_frequency[ch] = character_frequency.get(ch, 0) + 1

        odd_frequency = {}
        max_odd_frequency = 0
        for ch, frequency in character_frequency.items():
            if frequency % 2 == 1:
                odd_frequency[ch] = frequency
                if frequency > max_odd_frequency:
                    max_odd_frequency = frequency

        even_frequency = {}
        min_even_frequency = float('inf')
        for ch, frequency in character_frequency.items():
            if frequency % 2 == 0:
                even_frequency[ch] = frequency
                if frequency < min_even_frequency:
                    min_even_frequency = frequency

        diff = max_odd_frequency - min_even_frequency

        return diff