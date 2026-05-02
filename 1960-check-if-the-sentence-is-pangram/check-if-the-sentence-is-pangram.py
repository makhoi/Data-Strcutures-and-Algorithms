class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = set()
        for ch in range(ord('a'), ord('z') + 1):
            alphabets.add(chr(ch))

        characters = set()
        for ch in sentence:
            characters.add(ch)

        return alphabets == characters