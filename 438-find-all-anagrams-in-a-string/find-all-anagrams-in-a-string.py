class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = {} # p_character_frequency
        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1
        
        res = []
        s_count = {}
        left = 0

        for right in range(len(s)):
            s_count[s[right]] = s_count.get(s[right], 0) + 1

            while right - left + 1 > len(p):
                s_count[s[left]] -= 1
                if s_count[s[left]] == 0:
                    del s_count[s[left]]
                left += 1

            if s_count == p_count:
                res.append(left)

        return res