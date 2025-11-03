class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        
        magazin_map = {}

        for element in magazine: 
            if element not in magazin_map: 
                magazin_map[element] = 1
            magazin_map[element] += 1

        ransomNote_map = {}

        for element in ransomNote:
            if element not in ransomNote_map: 
                ransomNote_map[element] = 1
            ransomNote_map[element] += 1


        for key,value in ransomNote_map.items():
            if key not in magazin_map:
                return False
            else: 
                if value > magazin_map[key]:
                    return False
        return True