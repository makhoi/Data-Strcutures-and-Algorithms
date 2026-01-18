class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        num_to_frequency = {}
        for num in nums:
            num_to_frequency[num] = num_to_frequency.get(num, 0) + 1

        for frequency in num_to_frequency.values():
            if frequency == 1:
                continue

            is_prime = True
            for i in range(2, int(frequency**0.5)+1):
                if frequency % i == 0:
                    is_prime = False
                    break
            if is_prime == True:
                return True

        return False