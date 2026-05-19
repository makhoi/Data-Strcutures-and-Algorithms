class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        n = len(s)
        res_index = -1
        vowels = ('a', 'e', 'i', 'o', 'u')

        for i in range(n-1, -1, -1):
            if s[i] not in vowels:
                res_index = i
                break
                
        if res_index != -1:
            return s[:res_index+1]
        else:
            return ""