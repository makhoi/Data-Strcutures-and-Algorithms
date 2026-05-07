class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        max_length = 0
        total = sum(nums)
        length = len(nums)
        s = 0
        s_index = {}

        if total == x:
            return len(nums)

        for i in range(n):
            s += nums[i]

            if s == total - x:
                max_length = max(max_length, i + 1)

            if s - (total - x) in s_index:
                jM1 = s_index[s-(total-x)]
                j = jM1 + 1
                max_length = max(max_length, i - j + 1)

            if s not in s_index:
                s_index[s] = i

        return (length - max_length) if max_length else -1