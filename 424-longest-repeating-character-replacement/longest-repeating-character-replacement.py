# Sliding window type 1a 
# Time: O(n)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        frequency = {}

        for r in range(len(s)):
            frequency[s[r]] = frequency.get(s[r], 0) + 1

            while (r-l+1) - max(frequency.values()) > k: 
                frequency[s[l]] -= 1
                if frequency[s[l]] == 0:
                    del frequency[s[l]]
                l += 1

            res = max(res, r - l + 1)
        
        return res