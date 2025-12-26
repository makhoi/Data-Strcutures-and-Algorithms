class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        n = 0
        for i in range(len(digits)-1, -1, -1):
            number += digits[i] * pow(10, n)
            n += 1
        
        add_one = number + 1
        result = []
        for num in str(add_one):
            result.append(int(num))

        return result