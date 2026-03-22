class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        eating speed = k = # of banana/hour
        def canEat(k)

        piles = [3,6,7,11], h = 8
        canEat(1) -> F
        canEat(2) -> F
        canEat(3) -> F
        canEat(4) -> T
        canEat(5) -> T
        canEat(6) -> T
        --> find the first k that makes canEat(k) returns TRUE
        
        0. binary search: 
        tính tăng dần ?: index or k tăng dần? yes?
        tính liên tiếp: nếu canEat(k) là True thì tất cả các canEat(k) về sau đều là True, k tăng dần 
        -> binary search problem: yes
        1. basic/modified/adhoc: biến đổi từ đề thành array FFTTT -> adhoc
        2. lowerbound vs upperbound: lowerbound 
        3. search space: 1 -> max(piles)
        4. condition to move right: 

        ----------------------------------
        l               m                r
                        m -> T: move r to m
                        m -> False: move l to m + 1
        5. result: return l 
        '''

        def canEat(k): 
            total_hours = 0
            '''
            takes in k - eating speed -> how to find total hours?
            lets say k = 3 -> total hours = 1 + 2 + 3 + 4 = 10
                                          = (piles[0]/k + 1 if piles[0]%k != 0) + (piles[1]/k + 1 if piles[1]%k != 0) + (piles[2]/k + 1 if piles[2]%k != 0) 
            '''
            for i in range(len(piles)): 
                total_hours += piles[i]//k + (1 if piles[i]%k != 0 else 0)
            
            return total_hours <= h # if total_hours less or equal to h return True else False

        l = 1
        r = max(piles)

        while l < r: 
            m = l + (r-l)//2

            if canEat(m) == True:
                r = m
            else: 
                l = m + 1
        
        return l