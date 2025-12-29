class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # process given message to character seperated by , and no duplicate 
        key_no_duplicate = []
        for ch in key: 
            if ch == " ":
                continue
            if ch in key_no_duplicate:
                continue
            key_no_duplicate.append(ch)
        
        # map each character to alphabet letter
        alphabet_map = {}
        alphabet = ord('a')
        for ch in key_no_duplicate:
            alphabet_map[ch] = chr(alphabet)
            alphabet += 1 
        
        # decode message
        decode_message = []
        for ch in message: 
            if ch == " ":
                decode_message.append(" ")
            else: 
                decode_message.append(alphabet_map[ch])
        
        return "".join(decode_message)


            