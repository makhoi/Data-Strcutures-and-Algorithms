class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        what is the condition to stop the expanding window? 
        
        '''
        l = 0
        window = []
        res = []

        original = {}
        window = {}

        for i in range(len(p)):
            original[p[i]] = original.get(p[i], 0) + 1

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            while r - l + 1 > len(p):
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
            
            if r - l + 1 == len(p):
                if window == original:
                    res.append(l)

        return res