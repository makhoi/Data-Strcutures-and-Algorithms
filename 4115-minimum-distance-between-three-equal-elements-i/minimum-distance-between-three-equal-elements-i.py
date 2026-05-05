class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return -1

        distances = []
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] == nums[j] == nums[k]:
                        distances.append(abs(i-j) + abs(j-k) + abs(k-i))
        return min(distances) if len(distances) else -1