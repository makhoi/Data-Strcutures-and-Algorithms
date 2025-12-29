class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    good_pairs.append((i,j))
        return len(good_pairs)
