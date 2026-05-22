class Solution:
    def scoreBalance(self, s: str) -> bool:
        letter_value = {chr(ord('a') + i): i + 1 for i in range(26)}

        n = len(s)
        prefix_sum = [0]*n
        prefix_sum[0] = letter_value[s[0]]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + letter_value[s[i]]

        def sumRange(start, end):
            return prefix_sum[end] - (prefix_sum[start - 1] if start else 0)

        for i in range(n):
            if sumRange(0,i) == sumRange(i+1,n-1):
                return True

        return False