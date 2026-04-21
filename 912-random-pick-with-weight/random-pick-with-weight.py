class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total = prefix_sum

    def pickIndex(self) -> int:
        target = self.total * random.random()

        n = len(self.prefix_sums)
        left = 0
        right = n - 1

        while left < right: 
            mid = left + (right-left) // 2

            if target < self.prefix_sums[mid]:
                right = mid
            else:
                left = mid + 1
        return left