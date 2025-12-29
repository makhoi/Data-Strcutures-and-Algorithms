class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # process the given key to separate character with , and no duplicate
        key_no_duplicate = set()
        for ch in sentence: 
            key_no_duplicate.add(ch)

        # set of alphabet letters 
        alphabets = set()
        for ch in range(ord('a'), ord('z') + 1):
            alphabets.add(chr(ch))

        if key_no_duplicate == alphabets: 
            return True
        return False
        
        
        