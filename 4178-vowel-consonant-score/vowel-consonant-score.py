class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = {'a','e','i','o','u'}
        consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm','n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
        v = 0
        c = 0
        for ch in s:
            if ch in vowels:
                v += 1
            elif ch in consonants:
                c += 1
            else:
                continue
        if c:
            score = math.floor(v/c)
        else:
            score = 0
        
        return score