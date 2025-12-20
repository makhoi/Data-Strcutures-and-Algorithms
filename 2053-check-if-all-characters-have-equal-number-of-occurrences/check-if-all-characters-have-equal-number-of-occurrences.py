class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:        
        if len(set(s)) == 1:
            return True

        seen = set()
        unique_chars = []

        for c in s: 
            if c in seen:
                continue

            seen.add(c)
            unique_chars.append(c)

        frequency = {}
        
        for c in s: 
            frequency[c] = frequency.get(c, 0) + 1

        for index in range(1, len(unique_chars)):
            if frequency[unique_chars[index]] != frequency[unique_chars[index-1]]:
                return False
        return True


        