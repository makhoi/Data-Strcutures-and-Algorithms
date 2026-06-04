class Solution:
    def maxDifference(self, s: str) -> int:
        character_frequency = {}
        for ch in s:
            character_frequency[ch] = character_frequency.get(ch, 0) + 1

        max_odd = float('-inf')
        min_even = float('inf')
        for frequency in character_frequency.values():
            if frequency % 2 == 1 and frequency > max_odd:
                max_odd = frequency

            elif frequency % 2 == 0 and frequency < min_even:
                min_even = frequency

        return max_odd - min_even