# SLIDING WINDOW    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        sett = set() 

        for right in range(len(s)): 
            while s[right] in sett: # n TIMES total not per iteration of r
                sett.remove(s[left])
                left += 1

            width = (right - left) + 1 
            longest = max(longest, width)
            sett.add(s[right])

        return longest

        