class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:

        num_frequency = {}
        for num in nums:
            num_frequency[num] = num_frequency.get(num, 0) + 1

        frequency_divisible_k = []
        for num, frequency in num_frequency.items():
            if frequency % k == 0:
                frequency_divisible_k.append(num)

        res = 0
        for num in frequency_divisible_k:
            res += num*num_frequency[num]
        
        return res