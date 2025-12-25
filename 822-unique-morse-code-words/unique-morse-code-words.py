class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # map alphabet letter with morse code
        alphabet_to_morse = {}

        morses = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        alphabet = ord('a')
        
        for morse in morses:
            alphabet_to_morse[chr(alphabet)] = morse
            alphabet += 1

        # Encode 
        encoded_words = []

        for word in words: 
            encoded = []
            for ch in word: 
                encoded.append(alphabet_to_morse[ch])
            encoded_words.append("".join(encoded))

        # Find number of unique morse code
        unique_code = set()

        for word in encoded_words:
            unique_code.add(word)

        return len(unique_code)
        