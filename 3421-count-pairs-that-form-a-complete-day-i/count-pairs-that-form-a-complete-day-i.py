class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        length_hours = len(hours)

        count = 0
        for i in range(length_hours):
            for j in range(i+1, length_hours):
                pair_sum = hours[i] + hours[j]
                if pair_sum % 24 == 0:
                    count += 1
        return count