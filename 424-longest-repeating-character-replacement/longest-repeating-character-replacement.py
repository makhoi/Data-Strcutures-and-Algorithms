class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        character_frequency = {}
        left = 0

        for right in range(len(s)):
            character_frequency[s[right]] = character_frequency.get(s[right], 0) + 1
            max_character = max(character_frequency, key = character_frequency.get)
            max_count = character_frequency[max_character]

            while (right - left + 1) - max_count > k:
                character_frequency[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res