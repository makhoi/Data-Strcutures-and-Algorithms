class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        00. Determine it is adhoc problem
        0. Understand the problem
        def can_eat(k):
            # function returns True if with k speed KoKo can finish all all the banana until the guard is back 
            # first write a function to calculate how many hours KoKo need to take to finish piles of banana with k speed 
            # FFFFFTTTTTTTTTT 
        1. lowerbound vs upperbound: find first T -> first appearance of the target -> lowerbound 
        2. search space: 1 -> max(piles)
        3. condition to move right: if can_eat(mid) == True 
        4. meaning of left: first k that can_eat(left) == True
        5. return left -> k
        '''
        def can_eat(k):
            total_hours = 0
            for pile in piles: 
                total_hours += pile // k 
                if pile%k != 0:
                    total_hours += 1
            return total_hours <= h

        '''
        Now we got function that can take in speed and return FFFTTTTT -> find the first T
        '''
        left = 1
        right = max(piles)

        while left < right: 
            mid = left + (right - left)//2

            if can_eat(mid) == True: 
                right = mid
            else: 
                left = mid + 1
        return left