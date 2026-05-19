class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n = len(s)
        left = 0
        right = n - 1

        while left <= right: 
            if s[left] == s[right]:
                return left
            left += 1
            right -= 1

        return -1