class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized_chars = []

        for ch in s:
            if ch.isalnum(): 
                lower_ch = ch.lower()
                normalized_chars.append(lower_ch)

        normalized = ''.join(normalized_chars)

        reverse_normalized = []
        for i in range(len(normalized)-1, -1, -1):
            reverse_normalized.append(normalized[i])

        reverse = ''.join(reverse_normalized)

        if reverse == normalized:
            return True
        return False

        