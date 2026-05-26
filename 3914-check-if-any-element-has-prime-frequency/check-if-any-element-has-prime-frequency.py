class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    return False
            return True

        number_frequency = {}
        for num in nums:
            number_frequency[num] = number_frequency.get(num, 0) + 1

        for frequency in number_frequency.values():
            if is_prime(frequency):
                return True
        
        return False