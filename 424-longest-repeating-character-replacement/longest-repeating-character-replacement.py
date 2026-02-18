class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        stop condition
        len(window) - most frequency of a character
        '''
        l = 0
        res = 0
        character_frequency = {}
        maxf = 0

        for r in range(len(s)):
            character_frequency[s[r]] = character_frequency.get(s[r], 0) + 1
            maxf = max(maxf, character_frequency[s[r]])

            while (r-l+1) - maxf > k:
                character_frequency[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res