class Solution:
    def hasSameDigits(self, s: str) -> bool:
        nums = [int(ch) for ch in s]

        while len(nums) > 2:
            next_nums = []
            for i in range(len(nums)-1):
                next_nums.append((nums[i]+nums[i+1])%10)
            nums = next_nums

        return nums[0] == nums[1]
        