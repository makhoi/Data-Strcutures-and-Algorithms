class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        average = sum(nums)/len(nums)
        x = math.floor(average) + 1
        while x in nums:
            x += 1
        if x <= 0:
            for i in range(1, 101):
                if i not in nums:
                    return i
        return x