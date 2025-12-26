class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # map alphabet letters with morse code
        alphabet_to_morse = {}

        morses = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        alphabet = ord('a')

        for morse in morses: 
            alphabet_to_morse[chr(alphabet)] = morse
            alphabet += 1
        
        # Encode words with morse code
        encoded_words = []

        for word in words: 
            encoded = []
            for ch in word: 
                encoded.append(alphabet_to_morse[ch])
            encoded_words.append("".join(encoded))
        
        # Add all the encoded words to a set called unique_encoded_words 
        # return length of that set and we got the result
        unique_encoded_words = set(encoded_words)
        return len(unique_encoded_words)
        