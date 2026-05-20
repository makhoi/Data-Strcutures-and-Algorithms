class Solution:
    def residuePrefixes(self, s: str) -> int:
        length = []
        for i in range(len(s)):
            length.append(i+1)
        
        distincts = []
        seen = set()
        for ch in s:
            if ch not in seen:
                seen.add(ch)
            distincts.append(len(seen))
        
        res = 0
        for i in range(len(s)):
            if distincts[i] == length[i] % 3:
                res += 1
        
        return res