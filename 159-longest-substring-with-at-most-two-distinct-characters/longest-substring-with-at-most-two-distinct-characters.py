class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res = 0
        character_frequency = {}
        left = 0

        for right in range(len(s)):

            while len(character_frequency) == 2 and s[right] not in character_frequency:
                character_frequency[s[left]] -= 1
                if character_frequency[s[left]] == 0:
                    del character_frequency[s[left]]
                left += 1
            
            character_frequency[s[right]] = character_frequency.get(s[right], 0) + 1

            res = max(res, right - left + 1)
            
        return res