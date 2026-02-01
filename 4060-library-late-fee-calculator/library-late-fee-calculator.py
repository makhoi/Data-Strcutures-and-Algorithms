class Solution:
    def lateFee(self, daysLate: List[int]) -> int:
        late_fee = 0
        for day in daysLate:
            if day == 1:
                late_fee += 1
            elif day >= 2 and day <= 5:
                late_fee += day * 2
            else:
                late_fee += day * 3

        return late_fee