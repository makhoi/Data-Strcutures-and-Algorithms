class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        reverse_map = {}

        for i in range(26):
            reverse_map[i] = chr(ord('z') - i)

        res = []

        for word in words:
            weight = 0
            for ch in word: 
                weight += weights[ord(ch)-97]
            res.append(reverse_map[weight % 26])
        
        return "".join(res)