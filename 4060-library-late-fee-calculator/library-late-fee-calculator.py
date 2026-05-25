class Solution:
    def lateFee(self, daysLate: List[int]) -> int:
        total = 0
        for day in daysLate:
            if day == 1:
                total += 1
            elif 2 <= day <= 5:
                total += 2*day
            else:
                total += 3*day
        return total