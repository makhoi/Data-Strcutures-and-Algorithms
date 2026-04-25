class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        1. Iterate over every element in the input to expanding the window: using a set to record every character we traversed
            1.1. Condition to stop expanding: we check if that character is already exist in the set. If yes:
                1.1.1. Remove s[left] until that deduplicating character no longer in the set
                1.1.2. Contracting the window
            1.2. Proceed with current valid window: since we are looking for longest substring, we are going to use function max() to compare the current result and length of current substring
        '''
        res = 0
        left = 0
        seen = set()

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])

            res = max(res, right - left + 1)
        return res 