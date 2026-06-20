class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        longest_time = events[0][1]

        if len(events) == 1:
            return events[0][0]

        res = events[0][0]
        
        for i in range(1, len(events)):
            push_time = events[i][1] - events[i-1][1]
            if push_time > longest_time:
                longest_time = push_time
                res = events[i][0]
            elif push_time == longest_time and events[i][0] < res:
                res = events[i][0]

        return res