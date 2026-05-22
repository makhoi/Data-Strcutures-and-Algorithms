class Solution:
    def scoreBalance(self, s: str) -> bool:
        total = sum(ord(char) - ord('a') + 1 for char in s)

        left_sum = 0
        for char in s:
            left_sum += ord(char) - ord('a') + 1
            right_sum = total - left_sum

            if right_sum == left_sum:
                return True
        return False