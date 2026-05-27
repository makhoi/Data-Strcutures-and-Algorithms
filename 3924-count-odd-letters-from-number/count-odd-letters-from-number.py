class Solution:
    def countOddLetters(self, n: int) -> int:
        number_letter = {
            "1" : "one",
            "2" : "two",
            "3" : "three",
            "4" : "four",
            "5" : "five",
            "6" : "six",
            "7" : "seven",
            "8" : "eight",
            "9" : "nine",
            "0" : "zero"
        }

        letter = []
        for num in str(n):
            letter.append(number_letter[num])
        
        letter = "".join(letter)

        character_frequency = {}
        for character in letter:
            character_frequency[character] = character_frequency.get(character, 0) + 1

        odd = 0
        for character, frequency in character_frequency.items():
            if frequency % 2 == 1:
                odd += 1

        return odd