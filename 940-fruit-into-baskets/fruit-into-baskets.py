class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        '''
        find longest substring with 2 distinct number 
        '''
        l = 0
        res = 0
        number_frequency = {}

        for r in range(len(fruits)):
            number_frequency[fruits[r]] = number_frequency.get(fruits[r], 0) + 1

            while len(number_frequency) == 3:
                number_frequency[fruits[l]] -= 1
                if number_frequency[fruits[l]] == 0:
                    del number_frequency[fruits[l]]
                l += 1
            res = max(res, r - l + 1)
        
        return res 