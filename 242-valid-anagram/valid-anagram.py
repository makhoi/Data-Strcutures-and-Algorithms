class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_frequency = {}
        for ch in s:
            s_frequency[ch] = s_frequency.get(ch, 0) + 1
        
        t_frequency = {}
        for ch in t:
            t_frequency[ch] = t_frequency.get(ch, 0) + 1
        
        if t_frequency == s_frequency:
            return True
        return False