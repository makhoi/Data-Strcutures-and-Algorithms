class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        '''
        0. base case:
        len(set(s)) to determine number of distinct character from s
        if len(set(s)) <= k: return 0

        1. delta = len(set(s)) - k: number of characters to remove from s
        2. character_frequency table to keep track of the frequency of character in s
        3. find the value with frequency equal or smaller than delta, remove that key
        '''

        distincts = set(s)
        if len(distincts) <= k:
            return 0
        
        char_to_remove = len(distincts) - k 
        deletion_count = 0

        char_frequency = {}
        for ch in s:
            char_frequency[ch] = char_frequency.get(ch, 0) + 1

        while char_to_remove:
            # find the key associated with smallest value 
            # count += smallest value
            # remove the key
            # repeat the process until char_to_remove = 0 which means there is no letter left to remove
            min_char = min(char_frequency, key=char_frequency.get)
            min_value = char_frequency[min_char]

            deletion_count += min_value

            del char_frequency[min_char]
            char_to_remove -= 1

        return deletion_count