class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_ransomNote = {}
        for note in ransomNote: 
            count_ransomNote[note] = count_ransomNote.get(note, 0) + 1

        count_magazine = {}
        for ch in magazine: 
            count_magazine[ch] = count_magazine.get(ch, 0) + 1

        for ch in count_ransomNote: 
            if ch not in count_magazine: 
                return False
            else: 
                if count_ransomNote[ch] > count_magazine[ch]: 
                    return False
        return True