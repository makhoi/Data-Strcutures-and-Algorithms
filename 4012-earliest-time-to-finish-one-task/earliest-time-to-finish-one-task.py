class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        total_time = 0
        min_time = float('inf')
        for i in range(len(tasks)):
            total_time = sum(tasks[i])
            min_time = min(min_time, total_time)
        return min_time