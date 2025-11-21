class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_frequency = {}
        for ch in stones: 
            stone_frequency[ch] = stone_frequency.get(ch, 0) + 1
        
        result = 0
        for ch in jewels: 
            if ch in stone_frequency: 
                result += stone_frequency[ch]
        
        return result