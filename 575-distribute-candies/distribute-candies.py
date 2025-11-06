class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candies = {}

        n = len(candyType) // 2

        for candy in candyType: 
            if candy not in candies: 
                candies[candy] = 1
            candies[candy] += 1

        if len(candies) == n:
            return n
        elif len(candies) > n: 
            return n
        else: 
            return len(candies)