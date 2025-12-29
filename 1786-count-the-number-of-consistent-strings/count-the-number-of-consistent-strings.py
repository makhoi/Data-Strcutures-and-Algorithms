class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_character = set()
        for ch in allowed: 
            allowed_character.add(ch)

        count = len(words)

        for word in words: 
            for ch in word: 
                if ch not in allowed_character:
                    count -= 1
                    break
        return count