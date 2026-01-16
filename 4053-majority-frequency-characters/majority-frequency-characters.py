class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        '''
        1. First hash map: key - character, value - frequency
        2. Second hash map: key - frequency, value - array of character (by iterating first hashmap)
        3. From second hash map, return key with value has largest length
        '''
        frequency = {}
        for ch in s: 
            frequency[ch] = frequency.get(ch,0) + 1

        reverse = defaultdict(set)
        for ch, f in frequency.items():
            reverse[f].add(ch)

        
        best_freq = None
        best_group = None
        best_size = -1

        for f, group in reverse.items():
            size = len(group)
            if size > best_size or (size == best_size and f > best_freq):
                best_size = size
                best_freq = f
                best_group = group

        return "".join(best_group)