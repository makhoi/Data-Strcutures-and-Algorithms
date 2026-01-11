class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        frequency = {}
        for num in nums: 
            frequency[num] = frequency.get(num, 0) + 1

        sum = 0
        for num in nums:
            if frequency[num] % k == 0: 
                sum += num

        return sum