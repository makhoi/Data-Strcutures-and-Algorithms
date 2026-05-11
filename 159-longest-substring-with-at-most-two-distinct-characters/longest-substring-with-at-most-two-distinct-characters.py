class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        '''
        contain at most 2 distinct character -> condition to stop the expansion: len(character_frequency) > 2
        '''
        res = 0
        character_frequency = {}
        left = 0

        for right in range(len(s)):
            character = s[right]
            character_frequency[character] = character_frequency.get(character, 0) + 1
            distinct = len(character_frequency)

            while distinct > 2:
                character_frequency[s[left]] -= 1
                if character_frequency[s[left]] == 0:
                    del character_frequency[s[left]]
                    distinct -= 1
                left += 1

            res = max(res, right - left + 1)

        return res