class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        nums_str = []
        for num in nums:
            nums_str.append(str(num))

        total = []
        for num in nums_str:
            s = 0
            for n in num:
                s += int(n)
            total.append(s)

        for i in range(len(total)):
            if total[i] == i:
                return i
        return -1