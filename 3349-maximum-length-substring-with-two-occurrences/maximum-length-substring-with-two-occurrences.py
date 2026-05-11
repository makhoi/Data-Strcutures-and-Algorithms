class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res = 0
        left = 0
        character_frequency = {}

        for right in range(len(s)):
            character_frequency[s[right]] = character_frequency.get(s[right], 0) + 1

            while character_frequency[s[right]] > 2:
                character_frequency[s[left]] -= 1
                if character_frequency[s[left]] == 0:
                    del character_frequency[s[left]]
                left += 1
            res = max(res, right - left + 1)

        return res