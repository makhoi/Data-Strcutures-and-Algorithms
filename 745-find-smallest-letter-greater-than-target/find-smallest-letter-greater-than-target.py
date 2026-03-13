class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        '''
        0. Binary Search? Yes 
        1. Lowerbound/Upperbound? 
        duplicate and latter letter -> upperbound
        2. search space
        0 -> n-1
        3. Condition to move left: 
        if target >= mid: 
            l = m
        else: 
            r = m - 1
        4. Meaning of l 
        max r satisfies condition
        5. result: 
        
        '''
        n = len(letters)
        l = 0
        r = n - 1

        while l < r:
            m = r - (r-l) // 2

            if ord(target) >= ord(letters[m]):
                l = m
            else:
                r = m - 1

        if letters[l] > target:
            return letters[l]
        else:
            return letters[(l + 1) % n]