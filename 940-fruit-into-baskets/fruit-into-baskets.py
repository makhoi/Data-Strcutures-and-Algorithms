class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        '''
        return maximum length of subarray that has at most 2 different integers 
        --> condition to stop the expansion: len(number_frequency) > 2
        '''
        res = 0
        number_frequency = {}
        left = 0

        for right in range(len(fruits)):
            number_frequency[fruits[right]] = number_frequency.get(fruits[right], 0) + 1

            while len(number_frequency) > 2:
                number_frequency[fruits[left]] -= 1
                if number_frequency[fruits[left]] == 0:
                    del number_frequency[fruits[left]]
                left += 1
            
            res = max(res, right - left + 1)
        
        return res