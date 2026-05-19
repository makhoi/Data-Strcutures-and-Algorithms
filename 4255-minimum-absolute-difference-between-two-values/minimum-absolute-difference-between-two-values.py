class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        n = len(nums)

        min_pair = float('inf')

        for i in range(n):
            if nums[i] != 1:
                continue
            for j in range(i+1, n):
                if nums[j] != 2: 
                    continue
                if nums[i] == 1 and nums[j] == 2:
                    if abs(i-j) < min_pair:
                        min_pair = abs(i-j)
        
        for i in range(n-1,-1,-1):
            if nums[i] != 1:
                continue
            for j in range(i-1, -1, -1):
                if nums[j] != 2:
                    continue
                if nums[i] == 1 and nums[j] == 2:
                    if abs(i-j) < min_pair:
                        min_pair = abs(i-j)

        return min_pair if min_pair != float('inf') else -1