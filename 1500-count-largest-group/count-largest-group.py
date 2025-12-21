from typing import Dict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        group_sizes: Dict[int, int] = {}

        for number in range(1, n + 1):
            digit_sum = self._sum_digits(number)

            if digit_sum not in group_sizes:
                group_sizes[digit_sum] = 0

            group_sizes[digit_sum] += 1

        max_size = 0
        for size in group_sizes.values():
            if size > max_size:
                max_size = size

        count_of_largest = 0
        for size in group_sizes.values():
            if size == max_size:
                count_of_largest += 1

        return count_of_largest

    def _sum_digits(self, number: int) -> int:
        total = 0

        while number > 0:
            digit = number % 10
            total += digit
            number //= 10

        return total
