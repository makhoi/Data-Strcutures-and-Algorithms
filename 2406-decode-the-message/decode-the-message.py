class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # ENCODE MESSAGE

        # split sentence into single characters 
        chars = []

        for c in key: 
            if c != " ":
                chars.append(c)
        
        # remove duplicate from chars 
        unique_chars = []
        seen = set()

        for c in chars: 
            if c in seen: 
                continue
            
            seen.add(c)
            unique_chars.append(c)
            

        # map each character in unique_chars to alphabet letters
        chars_map = {}
        alphabet = ord('a')

        for c in unique_chars: 
            chars_map[c] = chr(alphabet)
            alphabet += 1

        # DECODE 
        result = []

        for c in message: 
            if c == " ":
                result.append(" ")
            else:
                result.append(chars_map[c])

        return ''.join(result)
        