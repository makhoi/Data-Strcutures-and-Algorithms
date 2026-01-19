class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        vowel_frequency = {}
        consonant_frequency = {}
        for ch in s:
            if ch in vowels:
                vowel_frequency[ch] = vowel_frequency.get(ch, 0) + 1
            else:
                consonant_frequency[ch] = consonant_frequency.get(ch, 0) + 1

        best_vowel_frequency = max(vowel_frequency.values()) if vowel_frequency else 0
        best_consonant_frequency = max(consonant_frequency.values()) if consonant_frequency else 0

        return best_vowel_frequency + best_consonant_frequency 