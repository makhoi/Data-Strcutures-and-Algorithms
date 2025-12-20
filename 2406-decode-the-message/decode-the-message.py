class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # ENCODE
        chars_map = {}
        alphabet_letter = ord('a')

        for c in key: 
            if c == " ":
                continue

            if c not in chars_map: 
                chars_map[c] = chr(alphabet_letter)
                alphabet_letter += 1

        # DECODE
        result = []

        for c in message:
            if c == " ":
                result.append(c)
            else: 
                result.append(chars_map[c])
                
        return "".join(result)
