class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0

        for word in words: 
            if set(word) <= set(allowed):
                count += 1
        
        return count
        
# <= does not mean “smaller size”
# It means set inclusion
# Order, size, lexicographic value are irrelevant