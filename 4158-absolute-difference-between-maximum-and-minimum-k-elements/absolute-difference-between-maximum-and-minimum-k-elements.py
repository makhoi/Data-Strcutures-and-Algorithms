class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        n = sorted(nums)

        def sumMinK(m):
            k_smallest = []
            for i in range(k): 
                k_smallest.append(m[i])
            return sum(k_smallest)

        def sumMaxK(m):
            k_largest = []
            for i in range(len(m) - 1, len(m) - k - 1, -1):
                k_largest.append(m[i])
            return sum(k_largest)

        return abs(sumMinK(n) - sumMaxK(n))