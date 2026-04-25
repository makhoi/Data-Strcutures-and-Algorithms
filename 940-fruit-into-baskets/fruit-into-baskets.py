class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        integer_frequency = {}
        left = 0

        for right in range(len(fruits)):

            while len(integer_frequency) == 2 and fruits[right] not in integer_frequency:
                integer_frequency[fruits[left]] -= 1
                if integer_frequency[fruits[left]] == 0:
                    del integer_frequency[fruits[left]]
                left += 1
            
            integer_frequency[fruits[right]] = integer_frequency.get(fruits[right], 0) + 1

            res = max(res, right - left + 1)

        return res