class Solution:
    def minimumFlips(self, n: int) -> int:
        
        binary = bin(n)[2:]

        reverse = []
        for i in range(len(binary) - 1, -1, -1):
            reverse.append(binary[i])
        reverse = "".join(reverse)

        res = 0
        for i in range(len(binary)):
            if binary[i] != reverse[i]:
                res += 1
                
        return res