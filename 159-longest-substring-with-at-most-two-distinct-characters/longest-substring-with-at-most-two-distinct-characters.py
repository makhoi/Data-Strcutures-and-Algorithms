class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = 0
        res = 0
        character_frequency = {}

        for r in range(len(s)):
            character_frequency[s[r]] = character_frequency.get(s[r],0) + 1

            while len(character_frequency) == 3: 
                character_frequency[s[l]] -= 1
                if character_frequency[s[l]] == 0: 
                    del character_frequency[s[l]]
                l += 1
            
            res = max(res, r - l + 1)

        return res