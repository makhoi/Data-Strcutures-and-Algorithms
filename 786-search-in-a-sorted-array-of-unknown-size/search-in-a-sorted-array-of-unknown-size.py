class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left = 0
        right = 10**4 - 1

        while left < right:
            mid = left + (right - left)//2

            if reader.get(mid) >= target:
                right = mid
            else:
                left = mid + 1

        return left if reader.get(left) == target else -1