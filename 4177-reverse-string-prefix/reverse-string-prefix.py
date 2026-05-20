class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        flipped = []
        for i in range(k-1, -1, -1):
            flipped.append(s[i])
        
        unflipped = []
        for i in range(k, len(s)):
            unflipped.append(s[i])

        return "".join(flipped+unflipped)