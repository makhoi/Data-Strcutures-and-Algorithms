class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''
        If current + weight > capacity → new day, reset current.
        '''
        def can_ship(capacity):
            current_weight = 0
            day_count = 1 

            for weight in weights: 
                if current_weight + weight > capacity: 
                    day_count += 1
                    current_weight = 0
                current_weight += weight
            return day_count <= days

        '''
        1. adhoc: FFFFFTTTTT -> find the first capacity that makes function can_ship()returns T -> find first T
        2. lowerbound vs upperbound: find first T -> lowerbound
        3. search space: 
        - left: max(weights) -> cannot split a package
        - right: sum(weights) -> ship all packages within 1 day
        4. condition to move right: if can_ship(mid) == True
        5. meaning of left: min L satisfies the condition
        6. result: return l
        '''
        left = max(weights) 
        right = sum(weights)

        while left < right: 
            mid = left + (right-left)//2

            if can_ship(mid) == True: 
                right = mid
            else: 
                left = mid + 1

        return left