class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        number_frequency = {}
        left = 0

        for right in range(len(fruits)):

            while len(number_frequency) == 2 and fruits[right] not in number_frequency:
                number_frequency[fruits[left]] -= 1
                if number_frequency[fruits[left]] == 0:
                    del number_frequency[fruits[left]]
                left += 1

            number_frequency[fruits[right]] = number_frequency.get(fruits[right], 0) + 1

            res = max(res, right - left + 1)

        return res