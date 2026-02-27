# Time: O(n^2)
# Sliding window type 1 - longest substring / b - add before while loop 
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = 0
        res = 0 
        frequency = {}

        for r in range(len(s)): 
            frequency[s[r]] = frequency.get(s[r], 0) + 1

            while len(frequency) > 2:
                frequency[s[l]] -= 1
                if frequency[s[l]] == 0:
                    del frequency[s[l]]
                l += 1

            res = max(res, r - l + 1)
        
        return res