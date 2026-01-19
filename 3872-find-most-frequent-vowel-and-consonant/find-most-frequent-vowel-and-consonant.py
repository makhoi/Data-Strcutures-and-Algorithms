class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o','u'}

        vowel_frequency = {}
        for ch in s:
            if ch in vowels:
                vowel_frequency[ch] = vowel_frequency.get(ch, 0) + 1

        consonant_frequency = {}
        for ch in s:
            if ch not in vowels:
                consonant_frequency[ch] = consonant_frequency.get(ch, 0) + 1

        best_vowel_frequency = 0
        for _ in vowel_frequency:
            best_vowel = max(vowel_frequency, key=vowel_frequency.get) # find best key from vowel_frequency table
            best_vowel_frequency = vowel_frequency[best_vowel] # find best value

        best_consonant_frequency = 0
        for _ in consonant_frequency:
            best_consonant = max(consonant_frequency, key=consonant_frequency.get) 
            best_consonant_frequency = consonant_frequency[best_consonant]

        result = best_vowel_frequency + best_consonant_frequency

        return result