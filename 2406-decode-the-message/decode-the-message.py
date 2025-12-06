class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        substitution = {}
        x = ord('a')

        for ch in key: 
            if ch == ' ':
                continue
            if ch not in substitution: 
                substitution[ch] = chr(x)
                x += 1
            
        result = []
        for ch in message: 
            if ch == ' ':
                result.append(' ')
            else: 
                result.append(substitution[ch])
        
        return ''.join(result)
