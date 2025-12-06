class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = {
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z'}

        letters = set(sentence)

        if alphabet == letters: 
            return True
        return False
