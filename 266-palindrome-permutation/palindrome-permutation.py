class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        frequency = {}

        for index in range(len(s)):
            if s[index] not in frequency:
                frequency[s[index]] = 1
            else:
                frequency[s[index]] += 1
        count = 0
        for value in frequency.values():
            if value % 2 == 1:
                count += 1
        if count > 1:
            return False
        return True