from collections import Counter

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        return sum(num * frequency for num, frequency in Counter(nums).items() if frequency % k == 0)