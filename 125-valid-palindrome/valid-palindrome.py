class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized_chars = []

        for ch in s: 
            if ch.isalnum():
                lower_ch = ch.lower()
                normalized_chars.append(lower_ch)

        normalized = ''.join(normalized_chars)
        
        reverse_chars = []

        for i in range(len(normalized)-1, -1, -1):
            reverse_chars.append(normalized[i])
        
        reverse = ''.join(reverse_chars)
        
        if normalized == reverse:
            return True
        return False