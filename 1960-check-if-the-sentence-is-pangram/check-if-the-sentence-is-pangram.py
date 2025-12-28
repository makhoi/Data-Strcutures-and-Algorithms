class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = set()
        for ch in range(ord('a'), ord('z') + 1):
            alphabets.add(chr(ch))

        pangram = set()
        for ch in sentence: 
            pangram.add(ch)
        
        if alphabets != pangram:
            return False
        return True