class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:

        num_frequency = {}
        for num in nums:
            num_frequency[num] = num_frequency.get(num, 0) + 1

        res = 0
        for num, frequency in num_frequency.items():
            if frequency % k == 0:
                res += num*frequency
                
        return res