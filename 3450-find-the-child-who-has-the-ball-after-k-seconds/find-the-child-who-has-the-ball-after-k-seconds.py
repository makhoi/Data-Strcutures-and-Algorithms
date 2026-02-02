class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        cycle = 2 * (n-1)
        position = k % cycle

        if position <= n - 1:
            return position
        return cycle - position