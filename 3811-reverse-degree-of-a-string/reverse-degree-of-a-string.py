class Solution:
    def reverseDegree(self, s: str) -> int:
        letter_value = {}
        for i in range(26):
            letter_value[chr(ord('a') + i)] = 26 - i

        total = 0
        for i in range(len(s)):
            total += letter_value[s[i]]*(i+1)

        return total