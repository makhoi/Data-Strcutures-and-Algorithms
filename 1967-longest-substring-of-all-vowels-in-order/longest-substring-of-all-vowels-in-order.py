class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        res = 0
        length = 1
        distinct = 1

        for right in range(1, len(word)):
            if word[right] == word[right-1]:
                length += 1
            elif word[right] > word[right-1]:
                length += 1
                distinct += 1
            else:
                distinct = 1
                length = 1

            if distinct == 5:
                res = max(res, length)

        return res