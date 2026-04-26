class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        character_count = {}
        left = 0

        for right in range(len(s)):

            while character_count.get(s[right], 0) == 1:
                character_count[s[left]] -= 1
                if character_count[s[left]] == 0:
                    del character_count[s[left]]
                left += 1

            character_count[s[right]] = character_count.get(s[right], 0) + 1

            res = max(res, right - left + 1)
            
        return res